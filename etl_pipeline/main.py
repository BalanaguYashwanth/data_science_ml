from load import load_csv_data
from report import run_report
from db import save_insights

def main():
    df = load_csv_data()
    insights = run_report(df)
    save_insights(insights)

if __name__ == '__main__':
    main()