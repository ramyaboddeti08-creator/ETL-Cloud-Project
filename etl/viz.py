import os
import matplotlib.pyplot as plt


def create_report(df, report_folder):

    print("=" * 50)
    print("STEP 4 : GENERATE REPORT")
    print("=" * 50)

    os.makedirs(report_folder, exist_ok=True)

    # Create Bar Chart
    plt.figure(figsize=(8,5))

    plt.bar(
        df["customer_name"],
        df["amount"],
    )

    plt.title("Customer Amount Report")

    plt.xlabel("Customer")

    plt.ylabel("Amount")

    plt.xticks(rotation=45)

    image_path = os.path.join(
        report_folder,
        "customer_report.png"
    )

    plt.tight_layout()

    plt.savefig(image_path)

    plt.close()

    print("Chart Generated Successfully.")

    html_path = os.path.join(
        report_folder,
        "report.html"
    )

    with open(html_path, "w") as file:

        file.write("""
<html>
<head>
<title>ETL Report</title>
</head>

<body>

<h1>ETL Project Report</h1>

<h2>Dataset Summary</h2>

""")

        file.write(df.describe().to_html())

        file.write("""

<h2>Chart</h2>

<img src="customer_report.png" width="700">

</body>

</html>

""")

    print("HTML Report Generated.")

    return html_path