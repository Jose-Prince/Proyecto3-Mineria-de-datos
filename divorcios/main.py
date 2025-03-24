import pandas as pd
import pyreadstat

# Load .sav file
sav_file = "RESsr1X3WuQcTxhLVlyslBKGtHAXqSrH.sav"  # Change this to your file path
df, meta = pyreadstat.read_sav(sav_file)

# Save as CSV
df.to_csv("a12.csv", index=False)
print("Conversion complete: output.csv")


# 2W4N7bnfbaVntLsINTDXCUZ57oCLyC3o
# 20181226143330lNO5qooyMLWxGu8XJLL7BXprdvTjfO0q
# 20191129151703IbgVgHc5enyxiXopUTuxcrUzC5WPkzCr