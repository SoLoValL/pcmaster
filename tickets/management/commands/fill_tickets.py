from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from tickets.models import Ticket
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates sample tickets for demonstration'

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username='admin')
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User admin not found.'))
            return

        # Create test clients
        clients_data = [
            ('ivan@example.com', 'Иван', 'Петров'),
            ('maria@example.com', 'Мария', 'Сидорова'),
            ('alex@example.com', 'Алексей', 'Козлов'),
            ('elena@example.com', 'Елена', 'Новикова'),
            ('dmitry@example.com', 'Дмитрий', 'Волков'),
        ]

        clients = []
        for email, first_name, last_name in clients_data:
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'username': email.split('@')[0],
                    'first_name': first_name,
                    'last_name': last_name,
                },
            )
            if created:
                user.set_password('Password123!')
                user.save()
                self.stdout.write('  Client: {} {} ({})'.format(first_name, last_name, email))
            clients.append(user)

        now = timezone.now()

        tickets_data = [
            {
                'client': clients[0],
                'device_type': 'laptop',
                'problem': 'Ноутбук ASUS сильно греется и выключается во время игр. При работе в браузере тоже тёплый, но не выключается. Прошло примерно 2 года с последней чистки.',
                'preferred_at': now + timedelta(days=2, hours=4),
                'address': 'м. Тимирязевская, ул. Дмитровское ш., 4',
                'status': 'assigned',
            },
            {
                'client': clients[1],
                'device_type': 'pc',
                'problem': 'Компьютер не включается. Нажимаю кнопку — вентиляторы дёрнулись и всё. Блок питания, видимо, сгорел. Компьютер игровой, собран 2 года назад.',
                'preferred_at': now + timedelta(days=1),
                'address': 'м. Авиамоторная, ул. Авиамоторная, 25',
                'status': 'in_progress',
            },
            {
                'client': clients[2],
                'device_type': 'laptop',
                'problem': 'Разбился экран на ноутбуке Lenovo. Трещина по диагонали, изображение идёт, но с артефактами. Нужна замена матрицы.',
                'preferred_at': None,
                'address': '',
                'status': 'new',
            },
            {
                'client': clients[3],
                'device_type': 'pc',
                'problem': 'Нужно установить Windows 11 и драйверы на новый компьютер. Компьютер куплен в магазине, система не установлена. Есть установочная флешка.',
                'preferred_at': now + timedelta(days=3, hours=8),
                'address': 'м. Курская, ул. Курская, 18',
                'status': 'new',
            },
            {
                'client': clients[4],
                'device_type': 'pc',
                'problem': 'Компьютер начал тормозить, программы открываются по 30 секунд. Жёсткий диск старый (5 лет), думаю пора менять на SSD. Нужно перенести все данные.',
                'preferred_at': now + timedelta(days=5),
                'address': 'м. Спортивная, ул. Спортивная, 7',
                'status': 'done',
            },
            {
                'client': clients[0],
                'device_type': 'printer',
                'problem': 'Принтер HP LaserJet не печатает. Пишет ошибка печати и зависает. Картридж менял месяц назад — вроде помогло, но теперь снова проблема.',
                'preferred_at': None,
                'address': '',
                'status': 'closed',
            },
            {
                'client': clients[1],
                'device_type': 'pc',
                'problem': 'Нашёл на компьютере майнер! Вирус майнит криптовалюту, процессор загружен на 100% даже в простое. Антивирус Kaspersky не помог. Прошу удалить вредоносную программу.',
                'preferred_at': now + timedelta(hours=2),
                'address': 'м. Белорусская, ул. Тверская-Ямская, 12',
                'status': 'assigned',
            },
            {
                'client': clients[3],
                'device_type': 'laptop',
                'problem': 'Залила ноутбук кофе. Сразу выключила и выключила из розетки. Прошло 2 часа, но ноутбук не включается. Может ещё спасти?',
                'preferred_at': now + timedelta(hours=1),
                'address': 'м. Павелецкая, ул. Павельцкая, 3',
                'status': 'in_progress',
            },
        ]

        count = 0
        for data in tickets_data:
            ticket, created = Ticket.objects.get_or_create(
                client=data['client'],
                device_type=data['device_type'],
                problem=data['problem'],
                defaults={
                    'preferred_at': data['preferred_at'],
                    'address': data['address'],
                    'status': data['status'],
                },
            )
            if created:
                count += 1
                status_labels = dict(Ticket.STATUS_CHOICES)
                self.stdout.write(
                    '  Ticket #{}: {} {} - {}'.format(
                        ticket.pk,
                        data['client'].first_name,
                        data['client'].last_name,
                        status_labels[data['status']]
                    )
                )

        self.stdout.write(self.style.SUCCESS('\nDone! Created {} tickets.'.format(count)))
