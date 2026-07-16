from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework import permissions


class IsAuthorOrReadOnly(BasePermission):
    """Faqat muallif o'zgartirish kiritishi mumkin, boshqalar faqat o'qiy oladi."""
    
    def has_permission(self, request, view) -> bool:
        # Xavfsiz usullar (GET, HEAD, OPTIONS) uchun ruxsat berish
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Faqat autentifikatsiya qilingan foydalanuvchilar yaratish/tahrirlash/o'chirish huquqiga ega
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj) -> bool:
        # Xavfsiz usullar uchun ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Faqat muallif o'z postini tahrirlashi yoki o'chirishi mumkin
        return obj.author == request.user    
        
