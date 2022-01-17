
# read
with open('printing.script', 'r') as file :
  filedata = file.read()

# set feature
feature = 'Tray'

# pose transformation
filedata = filedata.replace(
    'movep(p', 'movep(pose_trans({feature},p'.format(feature=feature)
    )
filedata = filedata.replace(']', '])')

# write
with open('transformed_printing.script', 'w') as file:
  file.write(filedata)
