# Create a multi-level index
df_multi = df.set_index(['Region', 'Quarter'])

# Access data using a tuple of labels
df_multi.loc[('North', 'Q1')]
