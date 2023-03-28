import pandas as pd


class Customize:
    demand_type_list = ['1차 금속 제조업']


class ProbOptions(Customize):
    def __init__(self):
        # MW
        self.power_demand_max = 100

        self.loc_damand_factor = "data/1. 2021_표준산업분류(중분류),주택용 1_24시 상대계수.xlsx"
        self.loc_pv_factor_IC = "data/전남_한국서부_영암F1_2020_태양광.xlsx"


        self.choice_number_of_demand_type = 'customize'  # customize / all
        self.choice_region_gen = 'JN'



        self.set_demand_type_list()

    def set_demand_type_list(self):
        if self.choice_number_of_demand_type == 'customize':
            self.demand_type_list = Customize.demand_type_list

        elif self.choice_number_of_demand_type == 'all':
            self.demand_type_list = ['1차 금속 제조업', '가구 제조업', '고무제품 및 플라스틱제품 제조업']


class LoadInputFile:
    def __init__(self, options: ProbOptions):
        self.factor_demand_all_raw = pd.read_excel(options.loc_damand_factor)

        if options.choice_region_gen == 'JN':
            self.factor_gen_raw = pd.read_excel(options.loc_pv_factor_IC, sheet_name=None)