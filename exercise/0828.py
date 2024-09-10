import pandas as pd
import os

# file_path = f'.\738\STOCK_DAY_00738U_{}{}.csv'
# Define the base path and file pattern
base_path = r'.\738'
file_pattern = 'STOCK_DAY_00738U_{}{}.csv'

# Initialize an empty list to collect DataFrames
df_list = []

# Loop through each year
for year in range(2020, 2025):
    # Loop through each month of the year
    for month in range(1, 12):

        # Create the filename for each month
        filename = file_pattern.format(year, f'{month:02d}')
        file_path = os.path.join(base_path, filename)

        # Check if the file exists
        if os.path.exists(file_path):
            # Read the CSV file
            df = pd.read_csv(file_path, encoding='Big5', header=1, thousands=',')

            # Filter rows and process the DataFrame
            df = df[df['日期'].str.match(r'^\d{3}/\d{2}/\d{2}$')]
            df = df.drop(columns=['Unnamed: 9', '成交金額', '漲跌價差', '成交筆數'])
            df['成交股數'] = df['成交股數'].astype('uint32')

            # Append to the list of DataFrames
            df_list.append(df)
        else:
            print(f"File not found: {file_path}")

# Concatenate all DataFrames
df_all = pd.concat(df_list, ignore_index=True)

# Reset index of the concatenated DataFrame
df = df_all.reset_index(drop=True)

print(df.info())
# 白銀股價  日期	成交股數	開盤價	最高價	最低價	收盤價



import matplotlib.pyplot as plt
plt.rc('font', family='Microsoft JhengHei')

# Convert ROC dates to Gregorian dates
def convert_roc_to_gregorian(roc_date):
    year, month, day = map(int, roc_date.split('/'))
    gregorian_year = year + 1911
    return f'{gregorian_year}-{month:02d}-{day:02d}'
df['日期'] = df['日期'].apply(convert_roc_to_gregorian)
# Convert the '日期' column to datetime objects
df['日期'] = pd.to_datetime(df['日期'], format='%Y-%m-%d')

print(df['日期'].head(3))
print(df.info())

# Extract Date and Close columns
日期 = df['日期']
收盤價 = df['收盤價']

# Calculate 20-day moving average
df['20MA'] = df['收盤價'].rolling(window=20).mean()
df['60MA'] = df['收盤價'].rolling(window=60).mean()

# Create a figure and axes
_fig = plt.gcf()  #_fig object
_axes = plt.gca()

# Set figure and axes properties matplotlib color:float
_fig.set_facecolor((223/255, 223/255, 200/255))
_fig.set_figheight(7)
_fig.set_figwidth(20)  # Increased figure width
_fig.set_layout_engine(layout='tight')
_axes.set_facecolor('#dbc1ac')

# Plot the data
plt.title("元大白銀折線圖", fontsize=18)
plt.plot(日期, 收盤價, color=('black'), linewidth=2.0, marker='o', markerfacecolor='#ece0d1', label='收盤價')
plt.plot(日期, df['20MA'], color='blue', linestyle='--', linewidth=2.0, label='20日移動平均線')
plt.plot(日期, df['60MA'], color='red', linestyle='--', linewidth=2.0, label='60日移動平均線')


# Set x-ticks and labels
_xticks = df['日期'].iloc[::20]  # Adjust frequency as needed
_labels = _xticks.dt.strftime('%Y-%m-%d')  # Format x-tick labels
plt.xticks(ticks=_xticks, labels=_labels, rotation=45)  # Rotate labels

plt.xlabel("日期", fontsize=12)
plt.ylabel("收盤價", fontsize=12)
plt.grid(visible=True, axis='y', linestyle='-')
plt.legend()  # Add a legend to differentiate lines
plt.tight_layout()  # Adjust layout
plt.show()
# plt.savefig("元大白銀.pdf", dpi=300, bbox_inches="tight")
