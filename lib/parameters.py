import numpy as np
import pandas as pd


class Customize:
    demand_type_list = ['1차 금속 제조업']


class ProbOptions(Customize):
    def __init__(self):
        # MW
        self.power_demand_max = 100

        self.loc_damand_factor = "C:/Users/NEXTGroup/Dropbox/모델 개발/OptimalPortfolio/data/부하/1. 2021_표준산업분류(중분류),주택용 1_24시 상대계수.xlsx"
        self.loc_pv_factor_IC = "C:/Users/NEXTGroup/Dropbox/모델 개발/OptimalPortfolio/data/발전기/전남_한국서부_영암F1_2020_태양광.xlsx"


        self.choice_number_of_demand_type = 'customize'  # customize / all
        self.choice_region_gen = 'JN'



        self.set_demand_type_list()

    def set_demand_type_list(self):
        if self.choice_number_of_demand_type == 'customize':
            self.demand_type_list = Customize.demand_type_list

        elif self.choice_number_of_demand_type == 'all':
            self.demand_type_list = ['1차 금속 제조업', '가구 제조업', '고무제품 및 플라스틱제품 제조업']


class CallInput:
    def __init__(self, options: ProbOptions):
        month = 1
        self.month_to_row = dict()
        row = 0
        for d in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
            self.month_to_row[month] = np.arange(row, row + d, 1)
            row += d
            month += 1


        if options.choice_region_gen == 'JN':
            self.factor_gen_raw = pd.read_excel(options.loc_pv_factor_IC, sheet_name=None)

        self.call_dmd(options)
        self.call_gen(options)

    def call_dmd(self, options):
        raw = pd.read_excel(options.loc_damand_factor)
        self.factor_dmd_list = dict()

        for k in options.demand_type_list:
            demand_arr = np.zeros((365, 24))
            if raw[k].shape[0] == 288:
                for m in range(1, 13, 1):
                    demand_arr[self.month_to_row[m], :] = raw[k].loc[(m - 1) * 24: m * 24 - 1].values

            self.factor_dmd_list[k] = demand_arr / np.max(demand_arr)

    def call_gen(self, options):
        gen = np.zeros((365, 24))

        if options.choice_region_gen == 'JN':
            raw = pd.read_excel(options.loc_pv_factor_IC, sheet_name=None)
            raw1 = raw['Sheet1'].loc[:, 1:24] / raw['Sheet2'].iloc[0].iloc[0]
            raw1.columns = np.arange(0, 24, 1)

            for d in range(0, 365, 1):
                for h in range(0, 24, 1):
                    mean_ = raw1.loc[d, h]
                    std_ = np.std(raw1.loc[:, h].values)
                    gen[d, h] = abs(np.random.normal(loc=mean_, scale=std_))

        self.factor_gen = gen