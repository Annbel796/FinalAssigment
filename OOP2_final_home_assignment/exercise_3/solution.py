import pandas as pd
import os

def clean_sales_data(input_path, output_path):
    # Load dataset
    df = pd.read_csv(input_path)

    # Remove duplicate order IDs
    df = df.drop_duplicates(subset="order_id")

    # Remove rows with outliers in total_price (above 8000)
    df = df[df["total_price"] <= 8000]

    # Remove rows with empty product_list
    df = df.dropna(subset=["product_list"])

    # Convert order_date to a uniform datetime format
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Remove rows where order_date could not be converted
    df = df.dropna(subset=["order_date"])

    # Save the cleaned dataset to a new CSV file
    df.to_csv(output_path, index=False)

def main():
    input_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')
    output_path = os.path.join(os.path.dirname(__file__), 'cleaned_sales_data.csv')

    clean_sales_data(input_path, output_path)

    print(f"Original sales data file: {input_path}")
    print(f"Cleaned sales data saved to: {output_path}")

if __name__ == "__main__":
    main()


# Denna variabel kan du använda för att läsa in filen sales_data_v2.csv som liger i samma mapp som denna fil.
# input_path = os.path.join(os.path.dirname(__file__), 'sales_data_v2.csv')

# Denna variabel kan du använda för att skriva ut filen sales_output_v2.xlsx i samma mapp som denna fil.
# output_path = os.path.join(os.path.dirname(__file__), 'cleaned_order_data.csv')

# INSTRUKTIONER

# - Använd pandas för att:
#     - Ta bort rader med duplicerade ordernummer
#     - Ta bort rader some har outliers i sitt total_price (över 800)
#     - Ta bort rader som har tomma product_list
#     - Konvertera datum som är i annat format till en enhetlig skala
# - Spara ner den till en ny fil kallad cleaned_sales_data.csv