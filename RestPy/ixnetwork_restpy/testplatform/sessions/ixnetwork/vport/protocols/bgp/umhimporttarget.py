
# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
    
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UmhImportTarget(Base):
	"""The UmhImportTarget class encapsulates a required umhImportTarget node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the UmhImportTarget property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'umhImportTarget'

	def __init__(self, parent):
		super(UmhImportTarget, self).__init__(parent)

	@property
	def ImportTargetList(self):
		"""Configures import route target in case of UMH routes

		Returns:
			list(dict(arg1:str[as|asNumber2|ip],arg2:number,arg3:str,arg4:number,arg5:number,arg6:number,arg7:str))
		"""
		return self._get_attribute('importTargetList')
	@ImportTargetList.setter
	def ImportTargetList(self, value):
		self._set_attribute('importTargetList', value)
