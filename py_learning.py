import os
import time
source = ['D:\\projects', 'D:\\test']
target_dir = 'D:\\backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print('zip command is: ' + zip_command + '\nrunning')
if os.system(zip_command) == 0:
    print('done, backuped to ' + target)
else:
    print('backup failed')