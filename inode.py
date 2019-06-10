class Inode():

	def __init__(self, number, owner, group, f_type, permissions, last_modification, last_f_modification, last_access, disk_adresses, size, status, logical_device, number, reference_count):
		### These are the fields of the inode on disk
		self.number = number
		self.owner = owner
		self.group = group
		self.f_type = f_type
		self.permissions = permissions
		#last modification of this inode
		self.last_modification = last_modification
		#last modification of the inode's file
		self.last_f_modification = last_f_modification
		self.last_access = last_access
		#Number of links to the file
		self.links = links
		self.disk_adresses = disk_adresses
		self.size = size
		### The next fields are available to the incore inode
		# pag. 63
		self.status = status
		self.logical_device = logical_device
		# The position of this inode on the disk 
		self.number = number
		self.reference_count = reference_count

