import pandas as pd
import json

# Load data
df = pd.read_excel('occupation_salary.xlsx')

# replace suppressed values and convert salary to numeric
df['A_MEAN'] = pd.to_numeric(df['A_MEAN'].replace(['#', '*'], None), errors='coerce')

# split into three levels
major_df    = df[df['OCC_GROUP'] == 'major'].set_index('OCC_CODE')
minor_df    = df[df['OCC_GROUP'] == 'minor'].set_index('OCC_CODE')
detailed_df = df[df['OCC_GROUP'] == 'detailed']

def get_minor_code(code):
    # '11-1011' -> '11-1000'
    return code[:3] + code[3] + '000'

def get_major_code(code):
    # '11-1000' -> '11-0000'
    return code[:3] + '0000'

# Build root -> major -> minor -> detailed hierarchy
root = {'name': 'U.S. Workforce', 'children': []}
major_nodes = {}
minor_nodes = {}

for code, row in major_df.iterrows():
    node = {'name': row['OCC_TITLE'], 'salary': round(row['A_MEAN']) if pd.notna(row['A_MEAN']) else None, 'children': []}
    major_nodes[code] = node
    root['children'].append(node)

for code, row in minor_df.iterrows():
    major_code = get_major_code(code)
    if major_code in major_nodes:
        node = {'name': row['OCC_TITLE'], 'salary': round(row['A_MEAN']) if pd.notna(row['A_MEAN']) else None, 'children': []}
        minor_nodes[code] = node
        major_nodes[major_code]['children'].append(node)

for _, row in detailed_df.iterrows():
    minor_code = get_minor_code(row['OCC_CODE'])
    if minor_code in minor_nodes:
        node = {'name': row['OCC_TITLE'], 'value': int(row['TOT_EMP']), 'salary': round(row['A_MEAN']) if pd.notna(row['A_MEAN']) else None}
        minor_nodes[minor_code]['children'].append(node)

# Save to JSON
with open('workforce.json', 'w') as f:
    json.dump(root, f, indent=2)

print('workforce.json written successfully.')
print(f'  Major groups : {len(major_nodes)}')
print(f'  Minor groups : {len(minor_nodes)}')
print(f'  Leaf nodes   : {sum(len(v["children"]) for v in minor_nodes.values())}')
