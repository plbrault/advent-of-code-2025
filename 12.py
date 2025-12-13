import re

gifts  = [
            [list(gift) for gift in gift.split('\n')] for gift in
            '\n'.join([
                line.replace('\n','')
                for line in open('input.txt').readlines()
                    if not re.match(r'^\d\dx\d\d:.', line)
                    and not re.match(r'^\d:$', line)
            ]).split('\n\n')
        ]
regions = [
    (
        (
            int(region.split(' ')[0].split('x')[0]),
            int(region.split(' ')[0].split('x')[1].replace(':',''))
        ),
        [int(num_gifts) for num_gifts in region.split(' ')[1:]])
        for region in [
            line.replace('\n','')
            for line in open('input.txt').readlines() if re.match(r'^\d\dx\d\d:', line)
        ]
]

GIFT_SIZE = 9

solvable = []
unsolvable = []
unknown = []

for region in regions:
    total_gifts = sum(region[1])
    total_gift_size = total_gifts * GIFT_SIZE
    total_shape_parts = sum([
        num_gifts * sum([
            sum([ 1 for value in shape_row if value == '#' ])
            for shape_row in gifts[gift_id]
        ])
        for gift_id, num_gifts in enumerate(region[1])
    ])
    region_size = region[0][0] * region[0][1]
    if region_size >= total_gift_size:
        solvable.append(region)
    elif region_size < total_shape_parts:
        unsolvable.append(region)
    else:
        unknown.append(region)

print('Solvable regions:', len(solvable))
print('Unsolvable regions:', len(unsolvable))
print('Unknown:', len(unknown))
