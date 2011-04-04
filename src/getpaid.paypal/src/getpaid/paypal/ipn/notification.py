from UserDict import DictMixin

main_mapping = { 'address_city':'address_city',
                 'address_country':'address_country',
                 'address_country_code':'address_country_code',
                 'address_name':'address_name',
                 'address_state':'address_state',
                 'address_status':'address_status',
                 'address_street':'address_street',
                 'address_zip':'address_zip',
                 'first_name':'first_name',
                 'last_name':'last_name',
                 'payer_business_name':'business_name',
                 'payer_email':'email',
                 'payer_id':'payer_id',
                 'payer_status':'payer_status',
                 'contact_phone':'phone',
                 'residence_country':'residence_country',
                 'business':'my_business',
                 'receiver_email':'receiver_email',
                 'receiver_id':'receiver_id',
                 'custom':'custom',
                 'invoice':'invoice',
                 'memo':'memo',
                 'option_name_1':'option_name_1',
                 'option_name_2':'option_name_2',
                 'option_selection1':'option_selection1',
                 'option_selection2':'option_selection2',
                 'tax':'tax',
                 'auth_id':'auth_id',
                 'auth_exp':'auth_exp',
                 'auth_amount':'auth_amount',
                 'num_cart_items':'num_cart_items',
                 'parent_txn_id':'parent_txn_id',
                 'payment_date':'payment_date',
                 'payment_status':'payment_status',
                 'payment_type':'payment_type',
                 'pending_reason':'pending_reason',
                 'reason_code':'reason_code',
                 'remaining_settle':'remaining_settle',
                 'shipping_method':'shipping_method',
                 'shipping':'shipping',
                 'transaction_entity':'transaction_entity',
                 'txn_id':'txn_id',
                 'txn_type':'txn_type',
                 'exchange_rate':'exchange_rate',
                 'mc_currency':'mc_currency',
                 'mc_fee':'mc_fee',
                 'mc_gross':'mc_gross',
                 'mc_shipping#':'mc_total_shipping',
                 'mc_handling#':'mc_total_handling',
                 'payment_fee':'payment_fee',
                 'payment_gross':'payment_gross',
                 'settle_amount':'settle_amount',
                 'settle_currency':'settle_currency',
                 'test_ipn':'test_ipn',
                 }

auction_mapping = {'auction_buyer_id':'auction_buyer_id',
                   'auction_closing_date':'auction_closing_date',
                   'auction_multi_item':'auction_multi_item',
                   'for_auction':'for_auction',
                   }

subscription_mapping = {'subscr_date':'subscription_date',
                        'subscr_effective':'subscription_effective',
                        'period1':'subscription_period1',
                        'period2':'subscription_period2',
                        'period3':'subscription_period3',
                        'amount1':'subscription_amount1',
                        'amount2':'subscription_amount2',
                        'amount3':'subscription_amount3',
                        'mc_amount1':'subscription_mc_amount1',
                        'mc_amount2':'subscription_mc_amount2',
                        'mc_amount3':'subscription_mc_amount3',
                        'mc_currency':'subscription_mc_currency',
                        'recurring':'subscription_recurring',
                        'reattempt':'subscription_reattempt',
                        'retry_at':'subscription_retry_at',
                        'recur_times':'subscription_recur_times',
                        'username':'subscription_username',
                        'password':'subscription_password',
                        'subscr_id':'subscription_id',
                        }

dispute_mapping = {'case_id':'case_id',
                   'case_type':'case_type',
                   'case_creation_date':'case_creation_date',
                   'reason_code':'reason_code',
                   }

cart_item_mapping = {'item_name%s':'item_name',
                     'item_number%s':'item_number',
                     'quantity%s':'quantity',
                     'mc_gross%s':'mc_gross',
                     'mc_handling%s':'mc_handling',
                     'mc_shipping%s':'mc_shipping',
                     'option_name1%s':'option_name1',
                     'option_name2%s':'option_name2',
                     'option_selection1%s':'option_selection1',
                     'option_selection2%s':'option_selection2',
                     }

payment_txn_types = ['cart', 'express_checkout', 'merch_pmt', 'send_money', 
                     'virtual_terminal', 'web_accept']

subscription_txn_types = ['subscr-failed', 'subscr-cancel', 'subscr-payment', 
                          'subscr-signup', 'subscr-eot', 'subscr-modify']

dispute_txn_types = ['new_case', 'adjustment']

class CartItem(object):

    item_name = None
    item_number = None
    quantity = None
    mc_gross = None
    mc_handling = None
    mc_shipping = None
    option_name1 = None
    option_name2 = None
    option_selection1 = None
    option_selection2 = None

class Notification(DictMixin):
    
    shopping_cart = {}
    mass_payments = {}
    _form_variables = []

    def __init__(self, request = None):
        if request == None:
            return
        self.parse(request)
    
    def __repr__(self):
        return "<Notification at %s>" % id(self)

    # define a read-only dict interface to make it easier to work with upstream
    def __getitem__(self, item):
        return getattr(self, item)
    
    def __setitem__(self, item, value):
        return None
    
    def __delitem__(self, item):
        return None

    def keys(self):
        return self._form_variables
    # end of DictMixin classes

    def _do_parse(self, request, mapping):
        for item in mapping.keys():
            if request.has_key(item):
                self._form_variables.append(mapping[item])
                setattr(self, mapping[item], request[item])
            else:
                setattr(self, mapping[item], None)

    def parse(self, request):
        self._do_parse(request, main_mapping)
        
        # do specific parse methods for various types of IPN notifications
        if request.has_key('for_auction') and request['for_auction'] == 'true':
            self._parse_auction(request)
        
        if self.txn_type == 'cart':
            self._parse_cart(request)
        
        if self.txn_type == "masspay":
            self._parse_masspay(request)
            return
        
        if self.txn_type in subscription_txn_types:
            self._parse_subscription(request)
            return
        
        if self.txn_type in dispute_txn_types:
            self._parse_dispute(request)
            return
        
    def _parse_cart(self, request):
        self._form_variables.append('shopping_cart')
        if self.num_cart_items is not None:
            cartitems = range(1, int(self.num_cart_items)+1)
        else:
            cartitems = [1,]
        for i in cartitems:
            if request.has_key('item_number%s' % i):
                cartkey = request['item_number%s' % i]
            else:
                cartkey = "%s" % i
            self.shopping_cart[cartkey] = CartItem()
            for item in cart_item_mapping.keys():
                if request.has_key(item % i):
                    # parse out the shopping cart into each variable
                    setattr(self.shopping_cart[cartkey], cart_item_mapping[item], request[item % i])


    def _parse_auction(self, request):
        self._do_parse(request, auction_mapping)

    def _parse_subscription(self, request):
        self._do_parse(request, subscription_mapping)

    def _parse_masspay(self, request):
        """Stubbed out for now"""
    
    def _parse_dispute(self, request):
        self._do_parse(request, dispute_mapping)
