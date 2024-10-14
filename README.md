<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Student Performance Analysis</h1>
    <h2>Introduction</h2>
    <p>This project analyzes the academic performance of students based on several factors such as demographic, social, and academic attributes. The data is taken from a dataset that tracks various features of students, including family background, daily activities, and their final grades. The aim is to explore the relationship between these factors and the students' academic outcomes.</p>
    <h3>Dataset Description</h3>
    <p>The dataset used in this project contains the following columns:</p>
    <ul>
        <li><strong>school</strong>: The school of the student (binary: 'GP' or 'MS')</li>
        <li><strong>sex</strong>: Gender of the student ('F' or 'M')</li>
        <li><strong>age</strong>: Age of the student (numeric)</li>
        <li><strong>address</strong>: Type of address ('U' for urban, 'R' for rural)</li>
        <li><strong>famsize</strong>: Family size ('LE3' for less or equal to 3, 'GT3' for greater than 3)</li>
        <li><strong>Pstatus</strong>: Parent's cohabitation status ('T' for living together, 'A' for apart)</li>
        <li><strong>Medu</strong>: Mother's education (numeric: 0 to 4)</li>
        <li><strong>Fedu</strong>: Father's education (numeric: 0 to 4)</li>
        <li><strong>Mjob</strong>: Mother's job (nominal)</li>
        <li><strong>Fjob</strong>: Father's job (nominal)</li>
        <li><strong>reason</strong>: Reason to choose this school (nominal)</li>
        <li><strong>guardian</strong>: Student's guardian (nominal)</li>
        <li><strong>traveltime</strong>: Home to school travel time (numeric: 1 to 4)</li>
        <li><strong>studytime</strong>: Weekly study time (numeric: 1 to 4)</li>
        <li><strong>failures</strong>: Number of past class failures (numeric)</li>
        <li><strong>schoolsup</strong>: Extra educational support (binary: 'yes' or 'no')</li>
        <li><strong>famsup</strong>: Family educational support (binary: 'yes' or 'no')</li>
        <li><strong>paid</strong>: Extra paid classes (binary: 'yes' or 'no')</li>
        <li><strong>activities</strong>: Extra-curricular activities (binary: 'yes' or 'no')</li>
        <li><strong>nursery</strong>: Attended nursery school (binary: 'yes' or 'no')</li>
        <li><strong>higher</strong>: Wants to take higher education (binary: 'yes' or 'no')</li>
        <li><strong>internet</strong>: Internet access at home (binary: 'yes' or 'no')</li>
        <li><strong>romantic</strong>: In a romantic relationship (binary: 'yes' or 'no')</li>
        <li><strong>famrel</strong>: Quality of family relationships (numeric: 1 to 5)</li>
        <li><strong>freetime</strong>: Free time after school (numeric: 1 to 5)</li>
        <li><strong>goout</strong>: Going out with friends (numeric: 1 to 5)</li>
        <li><strong>Dalc</strong>: Workday alcohol consumption (numeric: 1 to 5)</li>
        <li><strong>Walc</strong>: Weekend alcohol consumption (numeric: 1 to 5)</li>
        <li><strong>health</strong>: Current health status (numeric: 1 to 5)</li>
        <li><strong>absences</strong>: Number of school absences (numeric)</li>
        <li><strong>G1</strong>, <strong>G2</strong>, <strong>G3</strong>: Grades in three periods (numeric: 0 to 20)</li>
    </ul>
    <h3>Numerical Analysis</h3>
    <p>The following numerical analyses were performed:</p>
    <ul>
        <li>Summary statistics (mean, median, etc.) of numeric columns such as <strong>age</strong>, <strong>absences</strong>, and <strong>grades (G1, G2, G3)</strong>.</li>
        <li>Correlation analysis between the numeric variables, specifically the relationships between factors like <strong>study time</strong>, <strong>failures</strong>, and final grades (<strong>G3</strong>).</li>
        <li>Head, Tail, Shape</li>
        <li>Distinct Value Count, Description</li>
        <li>Correlation Matrix, Corelation Heatmap</li>
        <li>Frequency Distribution of Categorical Columns</li>
        <li>Missing Value Analysis</li>
        <li>Variance & Standard Deviation of Numerical Columns</li>
        <li>Skewness & Kurtosis</li>
        <li>Outliers Detection using Z-Score</li>
        <li>Quantile Analysis</li>
        <li>Covariance</li>
        <li>Ratio of Variance f-Score</li>
    </ul>
    <h3>Data Visualization</h3>
    <p>The project includes the following visualizations:</p>
    <ul>
        <li><strong>Histogram of Grades</strong>: Distribution of final grades (<strong>G3</strong>) among students.</li>
        <li><strong>Box Plot</strong>: Comparison of grades based on factors like <strong>study time</strong>, <strong>internet access</strong>, and <strong>parental education</strong>.</li>
        <li><strong>Correlation Heatmap</strong>: Shows the correlation between different numerical features such as <strong>studytime</strong>, <strong>failures</strong>, and grades.</li>
        <li><strong>Pair Plot</strong></li>
        <li><strong>Density Heatmap</strong></li>
    </ul>
    <p><strong>Observations:</strong></p>
    <ul>
        <li>Students with more <strong>study time</strong> tend to have better final grades.</li>
        <li>Parental education, especially <strong>Medu</strong> (Mother's Education), has a positive correlation with student performance.</li>
        <li>Internet access and extra educational support show minimal direct impact on final grades.</li>
    </ul>
    <h3>Machine Learning Models</h3>
    <p>The following machine learning models were implemented to predict student performance based on the features in the dataset:</p>
    <table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>Algorithm</th>
                <th>Training Accuracy</th>
                <th>Validation Accuracy</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Logistic Regression</td>
                <td>0.7912</td>
                <td>0.7809</td>
            </tr>
            <tr>
                <td>Random Forest</td>
                <td>0.8242</td>
                <td>0.8000</td>
            </tr>
            <tr>
                <td>Gradient Boosting</td>
                <td>0.9707</td>
                <td>0.7524</td>
            </tr>
        </tbody>
    </table>
    <h2>Frontend Integration</h2>
    <p>This project is designed to eventually include a frontend interface for visualizing student performance and analyzing different factors interactively. The visualizations and predictions can be integrated into a web-based platform to allow teachers and students to gain insights into performance trends.</p>
    <h2>Conclusion</h2>
    <p>This analysis highlights how factors such as study habits, parental education, and family relationships influence student performance. The machine learning models provide a reasonable prediction of students' final grades based on these factors.</p>
</body>
</html>
