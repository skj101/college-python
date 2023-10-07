def sort_dict(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print('Original List:{}\n(asc):{}\n(dsc):{}'.format(colors,sort_dict(colors),sort_dict(colors, True)))

