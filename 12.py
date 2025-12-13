import re

regions = [
    (
        (
            int(region.split(' ')[0].split('x')[0]),
            int(region.split(' ')[0].split('x')[1].replace(':',''))
        ),
        [int(num_gifts) for num_gifts in region.split(' ')[1:]])
        for region in [
            line.replace('\n','')
            for line in open('input.txt').readlines() if re.match(r'^\d\dx\d\d:.+$', line)
        ]
]

print(regions)
