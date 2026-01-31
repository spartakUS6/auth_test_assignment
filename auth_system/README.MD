# RBAC система

## Архитектура
User → Role → Permission

- Пользователь может иметь несколько ролей
- Роль содержит набор разрешений
- Проверка доступа происходит по permission code

## Ошибки
- 401 — пользователь не аутентифицирован
- 403 — нет прав доступа

## Пример permissions
- reports.view
- admin.manage_roles
- admin.manage_permissions
