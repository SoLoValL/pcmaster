from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Заполняет сайт всеми начальными данными (услуги, блог, заявки)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Заполнение сайта...'))
        self.stdout.write('')

        self.stdout.write('[1/3] Загрузка услуг и навыков...')
        call_command('fill_services')

        self.stdout.write('')
        self.stdout.write('[2/3] Загрузка статей блога...')
        call_command('fill_blog')

        self.stdout.write('')
        self.stdout.write('[3/3] Создание примеров заявок...')
        call_command('fill_tickets')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write(self.style.SUCCESS('Сайт готов к работе!'))
        self.stdout.write(self.style.SUCCESS('=' * 50))
        self.stdout.write('')
        self.stdout.write('Админка: http://127.0.0.1:8000/admin/')
        self.stdout.write('Логин: admin / Пароль: Admin12345!')
        self.stdout.write('')
        self.stdout.write('Тестовые клиенты (для входа):')
        self.stdout.write('  ivan@example.com / Password123!')
        self.stdout.write('  maria@example.com / Password123!')
        self.stdout.write('  alex@example.com / Password123!')
