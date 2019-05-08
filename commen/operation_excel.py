import pandas


class OperationExcel:
    def __init__(self, file_path):
        self.table = pandas.read_excel(file_path)

    def get_data_info(self):
        """获取表格信息"""
        data = []
        for i in self.table.index.values:
            data_dict = self.table.loc[i].to_dict()
            data.append(data_dict)
        return data


if __name__ == '__main__':
    opera_excel = OperationExcel("../data/test_data.xlsx")
    print(opera_excel.get_data_info())
