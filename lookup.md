```python
import pandas as pd
```

# Create DF


```python
df = pd.DataFrame(data = {'A': ['Item 1','Item 2','Item 3'], 'B':['Item 3','Item 1','Item 2']})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Item 1</td>
      <td>Item 3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Item 2</td>
      <td>Item 1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Item 3</td>
      <td>Item 2</td>
    </tr>
  </tbody>
</table>
</div>



# Iterate through rows
This will find the first location of the value in column A in column B, and will then return the value in column A corresponding to the row in column B


```python
for index in df.iterrows():
    df.at[index[0],'C'] = df.loc[df['B'] == df.iloc[index[0]]['A'], 'A'].values[0]

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Item 1</td>
      <td>Item 3</td>
      <td>Item 2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Item 2</td>
      <td>Item 1</td>
      <td>Item 3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Item 3</td>
      <td>Item 2</td>
      <td>Item 1</td>
    </tr>
  </tbody>
</table>
</div>



# An Easier Breakdown to see what is happening


```python
for index in df.iterrows():
    value_looking_for = df.iloc[index[0]]['A']
    lookup_column = df['B']
    column_to_return = 'A'
    df.at[index[0],'C'] = df.loc[lookup_column == value_looking_for, column_to_return].values[0]

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Item 1</td>
      <td>Item 3</td>
      <td>Item 2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Item 2</td>
      <td>Item 1</td>
      <td>Item 3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Item 3</td>
      <td>Item 2</td>
      <td>Item 1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
