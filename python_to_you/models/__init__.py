from .user import User
from .role import Role
from .address import Address
from .profile import Profile, ProfilePicture
from .groups import Groups

from .categories import Category
from .post import Post, PostPicture
from .commit import Commit
from .like_dislike import LikeDislike

from .partner import Partner, PartnerImage

from .message import Message


User = User()
Role = Role()
Address = Address()
Profile = Profile() 
ProfilePicture = ProfilePicture()
Groups = Groups()
Category = Category()
Post = Post() 
PostPicture = PostPicture()
Commit = Commit()
LikeDislike = LikeDislike()
Partner = Partner() 
PartnerImage = PartnerImage()
Message = Message()