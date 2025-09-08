import pandas as pd
sheets=pd.DataFrame(pd.read_excel("Sample_sheet.xlsx"))


sheets.to_csv("Sample_sheet",index=None)

print(sheets)

print(f"Converted successfully csv")