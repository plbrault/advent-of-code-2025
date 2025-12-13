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



print(gifts)
