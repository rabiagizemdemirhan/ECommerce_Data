import os
from data_loader import load_data
from analysis import run_all_analysis 

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'data', 'turkiye_e_ticaret_simule_veri.csv')
    print("Loading data from:", data_path)

    df = load_data(data_path)
    
    print("First 5 Rows of the Dataset:")
    print(df.head())
    print("\nDataset Info:")
    df.info()

    run_all_analysis(df)

if __name__ == "__main__":
    main()
