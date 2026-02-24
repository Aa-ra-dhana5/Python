# import Package
# import Package.admin
# import Package.admin.service
# import Package.profile
# import Package.user
# import Package.user.name

from Package import *

obj = admin.service.Admin()
obj.show()

u = user.name.User()
u.show()

profile.show()
