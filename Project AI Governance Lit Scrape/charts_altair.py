import pandas as pd
import altair as alt
from pathlib import Path

# Load the dataset from the workspace subfolder
csv_path = Path('Project AI Governance Lit Scrape') / 'cities_ai_governance_dataset.csv'
df = pd.read_csv(csv_path)

# Use Tableau color palette for all categorical encodings
tableau_scale = alt.Scale(scheme='tableau10')

# Chart 1: Stacked bar by Year and Region
year_region = (
    alt.Chart(df)
    .transform_aggregate(
        count='count()',
        groupby=['Year', 'Region']
    )
    .mark_bar()
    .encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('count:Q', title='Number of Entries'),
        color=alt.Color('Region:N', scale=tableau_scale, legend=alt.Legend(title='Region')),
        tooltip=['Year:O', 'Region:N', 'count:Q']
    )
    .properties(
        title='AI Governance Entries by Year and Region',
        width=700,
        height=400
    )
)

# Chart 2: Horizontal bar chart of Discipline counts
discipline_counts = (
    df.groupby('Discipline', as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

discipline_chart = (
    alt.Chart(discipline_counts)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Discipline:N', sort='-x', title='Discipline'),
        color=alt.Color('Discipline:N', scale=tableau_scale, legend=None),
        tooltip=['Discipline:N', 'count:Q']
    )
    .properties(
        title='Entries by Discipline',
        width=700,
        height=330
    )
)

# Chart 3: Top Governance Type categories with grouping for smaller categories
lookup = df['Governance Type'].value_counts()
top_types = lookup.nlargest(10).index.tolist()
df['Governance Type Group'] = df['Governance Type'].where(df['Governance Type'].isin(top_types), 'Other')
governance_summary = (
    df.groupby('Governance Type Group', as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

governance_chart = (
    alt.Chart(governance_summary)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Governance Type Group:N', sort='-x', title='Governance Type'),
        color=alt.Color('Governance Type Group:N', scale=tableau_scale, legend=None),
        tooltip=['Governance Type Group:N', 'count:Q']
    )
    .properties(
        title='Top Governance Type Categories',
        width=700,
        height=380
    )
)

# Chart 4: Open Access and Scholar Gateway comparison
access_df = (
    df.melt(
        id_vars=[],
        value_vars=['Open Access', 'Scholar Gateway'],
        var_name='Indicator',
        value_name='Value'
    )
)

access_summary = (
    access_df.groupby(['Indicator', 'Value'], as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

access_chart = (
    alt.Chart(access_summary)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Value:N', title=None, sort='-x'),
        color=alt.Color('Value:N', scale=tableau_scale, legend=alt.Legend(title='Value')),
        column=alt.Column('Indicator:N', title=None),
        tooltip=['Indicator:N', 'Value:N', 'count:Q']
    )
    .properties(
        title='Open Access and Scholar Gateway Coverage',
        height=220,
        width=320
    )
)

import pandas as pd
import altair as alt
from pathlib import Path

# Enable PNG rendering for static image export
alt.renderers.enable('png')

# Load the dataset from the workspace subfolder
csv_path = Path('Project AI Governance Lit Scrape') / 'cities_ai_governance_dataset.csv'
df = pd.read_csv(csv_path)

# Use Tableau color palette for all categorical encodings
tableau_scale = alt.Scale(scheme='tableau10')

# Chart 1: Stacked bar by Year and Region
year_region = (
    alt.Chart(df)
    .transform_aggregate(
        count='count()',
        groupby=['Year', 'Region']
    )
    .mark_bar()
    .encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('count:Q', title='Number of Entries'),
        color=alt.Color('Region:N', scale=tableau_scale, legend=alt.Legend(title='Region')),
        tooltip=['Year:O', 'Region:N', 'count:Q']
    )
    .properties(
        title='AI Governance Entries by Year and Region',
        width=700,
        height=400
    )
)

# Chart 2: Horizontal bar chart of Discipline counts
discipline_counts = (
    df.groupby('Discipline', as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

discipline_chart = (
    alt.Chart(discipline_counts)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Discipline:N', sort='-x', title='Discipline'),
        color=alt.Color('Discipline:N', scale=tableau_scale, legend=None),
        tooltip=['Discipline:N', 'count:Q']
    )
    .properties(
        title='Entries by Discipline',
        width=700,
        height=330
    )
)

# Chart 3: Top Governance Type categories with grouping for smaller categories
lookup = df['Governance Type'].value_counts()
top_types = lookup.nlargest(10).index.tolist()
df['Governance Type Group'] = df['Governance Type'].where(df['Governance Type'].isin(top_types), 'Other')
governance_summary = (
    df.groupby('Governance Type Group', as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

governance_chart = (
    alt.Chart(governance_summary)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Governance Type Group:N', sort='-x', title='Governance Type'),
        color=alt.Color('Governance Type Group:N', scale=tableau_scale, legend=None),
        tooltip=['Governance Type Group:N', 'count:Q']
    )
    .properties(
        title='Top Governance Type Categories',
        width=700,
        height=380
    )
)

# Chart 4: Open Access and Scholar Gateway comparison
access_df = (
    df.melt(
        id_vars=[],
        value_vars=['Open Access', 'Scholar Gateway'],
        var_name='Indicator',
        value_name='Value'
    )
)

access_summary = (
    access_df.groupby(['Indicator', 'Value'], as_index=False)
    .size()
    .rename(columns={'size': 'count'})
)

access_chart = (
    alt.Chart(access_summary)
    .mark_bar()
    .encode(
        x=alt.X('count:Q', title='Number of Entries'),
        y=alt.Y('Value:N', title=None, sort='-x'),
        color=alt.Color('Value:N', scale=tableau_scale, legend=alt.Legend(title='Value')),
        column=alt.Column('Indicator:N', title=None),
        tooltip=['Indicator:N', 'Value:N', 'count:Q']
    )
    .properties(
        title='Open Access and Scholar Gateway Coverage',
        height=220,
        width=320
    )
)

# Save each chart as PNG
year_region.save('year_region_chart.png')
discipline_chart.save('discipline_chart.png')
governance_chart.save('governance_chart.png')
access_chart.save('access_chart.png')

print('Saved Altair charts as PNG files:')
print('- year_region_chart.png')
print('- discipline_chart.png')
print('- governance_chart.png')
print('- access_chart.png')

