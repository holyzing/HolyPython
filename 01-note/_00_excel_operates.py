# -*- encoding: utf-8 -*-
"""
第二个         第一个
A              C
B              C
C              A
D              这个没有直接对应，需要根据车牌判断一下
E              L
F              M
G              F
H              B
I              K
J              D
K              全部“未审核”
L-Q            全空
R              A中超链接的url
"""

# from openpyxl import load_workbook
import pandas as pd
import json
import sys

def hjy():
    e1 = pd.read_excel("backup.xls")
    # e2 = pd.read_excel("违章查询-20191028161126.xls", header=None)

    e1_c = e1.columns
    # e2_c = e2.iloc[1].values
    e2_c = ['卡口名称', '抓拍地点', '车牌号码', '归属地', '车速', '违章类型', '车辆类型', '车牌颜色', '车身颜色', '抓拍时间', '状态', '图片1', '图片2', '图片3', '图片4', '图片5', '图片6', '合成图片']

    A_M = list(map(lambda x:(chr(x)), range(ord('A'), ord('M') + 1)))
    A_R = list(map(lambda x:(chr(x)), range(ord('A'), ord('R') + 1)))

    e1.columns = A_M

    dependence = dict(zip(A_R, ["C", "C", "A", "归属地", "L", "M", "F", "B", "K", "D", "未审核", None, None, None, None, None, None, "合成图片"]))

    df = pd.DataFrame(columns=A_R)

    for k,v in dependence.items():
        if isinstance(v, str) and len(v) == 1:
            df[k] = e1[v]
        elif v is None:
            df[k] = ""
        elif v == "未审核":
            df[k] = "未审核"
        elif v == "归属地":
            df[k] = ""  # 修改的是所有列的值
        elif v == "合成图片":
            df[k] = ""
            pass

    with open("car_num.json", encoding="utf-8") as f:
        car_ids = json.load(f)

    car_ids = pd.DataFrame(car_ids)

# drop(inplace=True)  ：删除行

# iterrows：数据的dtype可能不是按行匹配的，因为iterrows返回一个系列的每一行，它不会保留行的dtypes(dtypes跨DataFrames列保留)*
# iterrows：不要修改行
# for index, row in df.iterrows():
#     car_id = row["C"]c

# Iterate over DataFrame rows as namedtuples.
# for row in df.itertuples(): # Pandas 的实例，tuple是不能更改的
#     car_id = row.C

def zjl_excel():
    df = pd.read_excel("excel/郑金霖.XLS")
    # TODO 正则直接处理 match 分组匹配 
    df["反转"] = df["在用卡号"].apply(lambda x: (x[-2:]+x[-4:-2]+x[-6:-4]+x[-8:-6]) if (isinstance(x,str) and len(x)==16) else "")
    df["转化"] = df["反转"].apply(lambda x: str(int(x, base=16)) if (isinstance(x,str) and len(x)==8) else "")
    df.to_excel("excel/zjl.xls", index=False)

def get_location(car_id):
    # car_id = row["C"]
    try:
        if len(car_id) >= 2:
            # location = car_ids.query('code=="%s"'%car_id[0:2])
            location = car_ids[car_ids.code == car_id[0:2]]  # 返回的是一个 dataframe
            if location is not None and len(location) == 1:  # TypeError: object of type 'int' has no len() 处理超链接 需要点击
                id_map = location.iloc[0]
                res = id_map["province"] + " " + id_map["city"]
                return res
            else:
                return car_id
        else:
            return car_id
    except TypeError as t:
        print("请随机点击Excel中的超链接，然后重试！")
        sys.exit()
    # 调用 apply 函数有三种方式。

    df["D"] = df["C"].apply(get_location)
    df["J"] = df["J"].apply(lambda x:x.split(".")[0])
    df.columns = e2_c
    df.to_excel("new.xls", sheet_name="clean", index=False)

    # writer = pd.ExcelWriter("backup.xls") # Append mode is not supported with xlwt(default engine)!
    # writer.save()
    # writer.close()

def append_df_to_excel(filename, df, sheet_name='Sheet1', startrow=None,
                       truncate_sheet=False,
                       **to_excel_kwargs):
    """
    Append a DataFrame [df] to existing Excel file [filename]
    into [sheet_name] Sheet.
    If [filename] doesn't exist, then this function will create it.
    Parameters:
      filename : File path or existing ExcelWriter
                 (Example: '/path/to/file.xlsx')
      df : dataframe to save to workbook
      sheet_name : Name of sheet which will contain DataFrame.
                   (default: 'Sheet1')
      startrow : upper left cell row to dump data frame.
                 Per default (startrow=None) calculate the last row
                 in the existing DF and write to the next row...
      truncate_sheet : truncate (remove and recreate) [sheet_name]
                       before writing DataFrame to Excel file
      to_excel_kwargs : arguments which will be passed to `DataFrame.to_excel()`
                        [can be dictionary]
    Returns: None
    """
   # from openpyxl import load_workbook

   # import pandas as pd

    # ignore [engine] parameter if it was passed
    if 'engine' in to_excel_kwargs:
        to_excel_kwargs.pop('engine')

    writer = pd.ExcelWriter(filename, engine='openpyxl')

    # Python 2.x: define [FileNotFoundError] exception if it doesn't exist
    try:
        FileNotFoundError
    except NameError:
        FileNotFoundError = IOError
    try:
        # try to open an existing workbook
        writer.book = load_workbook(filename)

        # get the last row in the existing Excel sheet
        # if it was not specified explicitly
        if startrow is None and sheet_name in writer.book.sheetnames:
            startrow = writer.book[sheet_name].max_row

        # truncate sheet
        if truncate_sheet and sheet_name in writer.book.sheetnames:
            # index of [sheet_name] sheet
            idx = writer.book.sheetnames.index(sheet_name)
            # remove [sheet_name]
            writer.book.remove(writer.book.worksheets[idx])
            # create an empty sheet [sheet_name] using old index
            writer.book.create_sheet(sheet_name, idx)

        # copy existing sheets
        writer.sheets = {ws.title:ws for ws in writer.book.worksheets}
    except FileNotFoundError:
        # file does not exist yet, we will create it
        pass

    if startrow is None:
        startrow = 0

    # write out the new sheet
    df.to_excel(writer, sheet_name, startrow=startrow, **to_excel_kwargs)

    # save the workbook
    writer.save()

if __name__ == "__main__":
    zjl_excel()