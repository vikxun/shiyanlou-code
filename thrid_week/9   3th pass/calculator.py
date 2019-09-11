#!/usr/bin/env python3

import sys
import csv



class Args(object):

    def __init__(self):

        self.argv = sys.argv[1:]
    
   
    def get_path(self, option):

        try:

            index = self.argv.index(option)

            return self.argv[index + 1]
        
        except (ValueError, IndexError):

            print('Parameter Error')

            exit()

    @property

    def config_path(self):

        return self.get_path('-c')

    @property

    def user_path(self):

        return self.get_path('-d')

    @property

    def export_path(self):

        return self.get_path('-o')

argv = Args()


class Config(object):
    
    def __init__(self):
    
        self.config = self._read_config()

    def _read_config(self):
        
        config = {}

        with open(argv.config_path) as f:

            for line in f.readlines():

                key, value = line.strip().split('=')

                try:

                    config[key.strip()]= float(value.strip())
                 
                except ValueError:

                    print('Parameter Error')

                    exit()
    
        return config

    def get_config(self,key):

        try:

            return self.config[key]

        except ValueError:

            print('Parameter Error')

            exit()

    @property

    def get_JiShuL(self):

       return self.get_config('JiShuL')

    @property

    def get_JiShuH(self):

        return self.get_config('JiShuH')

    @property

    def get_all_sum (self):

        return sum([self.get_config('YangLao'),
            self.get_config('YiLiao'),
            self.get_config('ShiYe'),
            self.get_config('GongShang'),
            self.get_config('ShengYu'),
            self.get_config('GongJiJin')])

config = Config()    

        
class UserData(object):
    
    def __init__ (self):
        
        self.userdata = self._read_userdata()

    def _read_userdata(self):
        
        userdata = []

        with open(argv.user_path) as f:

            for line in f.readlines():

                user_id, user_salary = line.strip().split(',')

                try:
                    income = int(user_salary)

                except ValueError:
                    
                    print('Parameter Error')
                    
                    exit()

                userdata.append((user_id, income))

            return userdata

    def __iter__(self):

        return iter(self.userdata)            


class IncomeTaxCalculator(object):

    def __init__(self, userdata):

        self.userdata = userdata
    
    @staticmethod
    
    def calc_shebao(income):

        if income < config.get_JiShuL:
            return config.get_JiShuL * config.get_all_sum
        elif income > config.get_JiShuH:
            return config.get_JiShuH * config.get_all_sum
        else:
            return income * config.get_all_sum
    
    @staticmethod

    def calc_nashui(shebao, income):
        
        shebao = float(shebao)

        if income <= 5000:
            real_nashui = 0
        else:
            should_nashui = float(income - shebao - 5000)

            if should_nashui > 0 and should_nashui <= 3000:
                real_nashui = should_nashui * 0.03
            elif should_nashui > 3000 and should_nashui <= 12000 :
                real_nashui = should_nashui * 0.10 - 210
            elif should_nashui > 12000 and should_nashui <=25000 :
                real_nashui = should_nashui * 0.20 - 1410
            elif should_nashui > 25000 and should_nashui <= 35000 :
                real_nashui = should_nashui * 0.25 - 2660
            elif should_nashui > 35000 and should_nashui <= 55000 :
                real_nashui = should_nashui * 0.30 - 4410
            elif should_nashui > 55000 and should_nashui <= 80000 :
                real_nashui = should_nashui * 0.35 - 7160 
            else:
                real_nashui = should_nashui * 0.45 - 15160
        return real_nashui



    @classmethod
    def calc_shuihou(cls,income):

        shebao = cls.calc_shebao(income)

        real_income = income - shebao - cls.calc_nashui(shebao, income)


        return real_income


    def calc_for_all_userdata(self):
        
        result = []

        for user_id, income in self.userdata:
            shebao = '{:.2f}'.format(self.calc_shebao(income))
            real_nashui = '{:.2f}'.format(self.calc_nashui(shebao, income))
            real_income = '{:.2f}'.format(self.calc_shuihou(income))
            result.append([user_id, income, shebao, real_nashui, real_income])
        return result

    def export(self, default = 'csv'):
        
        result = self.calc_for_all_userdata()

        with open(argv.export_path, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(result)


if __name__ == '__main__':
    
    calculator = IncomeTaxCalculator(UserData())
    
    calculator.export()

