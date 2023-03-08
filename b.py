# import openai as openai
#
# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)

budget_segments = '(29.4E8; 12/01/2022; 12/14/2022;); (29.4E8; 12/01/2022; 12/14/2022;); (29.4E8; 12/01/2022; 12/14/2022;); (29.4E8; 12/01/2022; 12/14/2022;);'
z = budget_segments
indexs_of_E = []
first_index = budget_segments.index('E')
i = 0
last_index_E = budget_segments.rindex('E')
while i < last_index_E:
    index = budget_segments.find('E', i + 1)
    i = index
    indexs_of_E.append(index)

for i in indexs_of_E:
    scientific_notation = budget_segments[i-first_index:i + 2].strip('(')
    number = str(float(scientific_notation))
    z = z.replace(scientific_notation, number)
budget_segments = z
print(budget_segments)