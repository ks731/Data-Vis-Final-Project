# The American Workforce
**U.S. Employment & Salary Across Occupational Groups**

An interactive treemap that shows which jobs employ the most Americans and how much they pay. Built with D3.js.

## How to Use
- **Click** any box to zoom into that group and see its sub-occupations
- **Hover** over any box to see the occupation name, total workers, and mean salary
- **Click the title** or use the breadcrumb trail at the top to go back
Box size = number of workers. Box color = mean annual salary (dark blue = low, orange-red = high).

## Files

```
├── index.html             # The visualization
├── workforce.json         # Data file used by the visualization
├── data_prep.py           # Script that generates workforce.json from the raw data
├── occupation_salary.xlsx # Raw dataset from Kaggle
└── README.md
```
## Running Locally
1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```

3. Open `http://localhost:8000` in your browser.

## Data
**Source:** BLS Occupational Employment and Wage Statistics, via Kaggle  
**URL:** https://www.kaggle.com/datasets/andrewmvd/occupation-salary-and-likelihood-of-automation  
**Dataset:** 1,394 rows × 20 columns
`data_prep.py` cleans the raw Excel file and converts it into the nested JSON format that D3 needs. It organizes occupations into three levels: major group → minor group → detailed occupation.

## Dependencies
- [D3.js v7](https://d3js.org/) — loaded automatically, nothing to install
- Python 3 with `pandas` and `openpyxl` — only needed if you want to regenerate `workforce.json`
