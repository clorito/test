import os
import time
source = ['D:\\projects', 'D:\\test']
target_dir = 'D:\\backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('enter a comment')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
    comment.replace(' ', '_') + '.zip' 
if not os.path.exists(today):
    os.mkdir(today)
    print('created', today)
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print('zip command is: ' + zip_command + '\nrunning')
if os.system(zip_command) == 0:
    print('done, backuped to ' + target)
else:
    print('backup failed')