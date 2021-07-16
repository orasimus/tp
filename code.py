import valohai as vh


if vh.parameters('example').value > 9000:
    print('Too powerful!')
    exit(1)

print('Let\'s go :)')
