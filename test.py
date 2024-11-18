class SoftDrikMarket:

    def __init__(self):
        self.current_leader = ""
        self.pepsi_product = []
        self.cocacola_product = []
        self.market_share = {}
        self.total_sales = 0

    
    def set_current_leader(self, current_leader):
        self.current_leader = current_leader
    
    def add_pepsi_product(self, p_product):
        self.pepsi_product.append(p_product)

    def add_coca_product(self, c_product):
        self.cocacola_product.append(c_product)
    
    def record_sales(self, coca_sales, pepsi_sales):

        self.total_sales = coca_sales + pepsi_sales
        market_sales_coca = coca_sales/self.total_sales * 100
        market_sales_pepsi = pepsi_sales/self.total_sales * 100

        self.market_share.update({"coca cola" : market_sales_coca})
        self.market_share.update({"pepsi": market_sales_pepsi})

        print(self.market_share.get("coca cola"))
        print(self.market_share.get("pepsi"))
        print(self.market_share)
        print(f'Total sales adalah {self.total_sales}, dengan market share coca : {market_sales_coca} % dan market share pepsi : {market_sales_pepsi} %')

    def check_leader(self):
        if self.market_share.get("coca cola") > self.market_share.get("pepsi"):
            self.current_leader = "coca cola"
        else:
            self.current_leader = "pepsi"

        return self.current_leader



sf = SoftDrikMarket()
sf.record_sales(20,30)
print(f'The leader on the marker is {sf.check_leader()}')

