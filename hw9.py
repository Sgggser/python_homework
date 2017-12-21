s = 'employee_first_name'

splitted = s.split('_')
s1 = splitted[0].capitalize()
s2 = splitted[1].capitalize()
s3 = splitted[2].capitalize()

s_cam_style = s1 + s2 + s3
print(s_cam_style)