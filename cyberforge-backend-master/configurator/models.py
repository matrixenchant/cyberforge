from django.db import models


class BaseModel(models.Model):
    TYPE_CHOICES = [
        ('Cooling', 'Cooling'),
        ('Memory', 'Memory'),
        ('Housing', 'Housing'),
        ('CPU', 'CPU'),
        ('Motherboard', 'Motherboard'),
        ('GPU', 'GPU'),
        ('RAM', 'RAM'),
        ('PowerSupplyUnit', 'PowerSupplyUnit'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, blank=True, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    images = models.ImageField(upload_to='static', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class Socket(models.Model):
    SOCKET_CHOICES = [
        ('LGA1150', 'LGA1150'),
        ('LGA1151', 'LGA1151'),
        ('LGA1155', 'LGA1155'),
        ('LGA1156', 'LGA1156'),
        ('LGA1200', 'LGA1200'),
        ('LGA1700', 'LGA1700'),
        ('LGA2011', 'LGA2011'),
        ('LGA2011 v3', 'LGA2011 v3'),
        ('LGA2066', 'LGA2066'),
        ('AM4', 'AM4'),
        ('sTR4', 'sTR4'),
    ]
    spec_labels = [
        {'slug': 'socket', 'label': 'Сокет'}
    ]
    socket = models.CharField(max_length=20, choices=SOCKET_CHOICES, unique=True)

    def __str__(self):
        return self.socket


class Cooling(BaseModel):
    TYPE_CHOICES = [
        ('CPU Cooler', 'CPU Cooler'),
        ('Case Fan', 'Case Fan'),
        ('Liquid Cooler', 'Liquid Cooler')
    ]

    spec_labels = [
        {'slug': 'cooling_type', 'label': 'Тип охлаждения'},
        {'slug': 'sockets', 'label': 'Сокеты'},
        {'slug': 'maximum_noise_level', 'label': 'Максимальный уровень шума'}
    ]

    cooling_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    sockets = models.ManyToManyField(Socket, related_name='sockets')
    maximum_noise_level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} type - {self.cooling_type} "


class Housing(BaseModel):
    mini = 'Mini Tower'
    midi = 'Midi Tower'
    full = 'Full Tower'

    CASE_FORM_FACTOR_CHOICES = [
        (mini, 'Mini Tower'),
        (midi, 'Midi Tower'),
        (full, 'Full Tower'),
    ]
    spec_labels = [
        {'slug': 'case_form_factor', 'label': 'Форм-фактор корпуса'},
        {'slug': 'compatible_board_form_factor', 'label': 'Форма-фактор материнкской платы'},
        {'slug': 'dimensions', 'label': 'Размеры'}
    ]

    case_form_factor = models.CharField(max_length=10, choices=CASE_FORM_FACTOR_CHOICES)
    compatible_board_form_factor = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=15, help_text='(WxHxD) in cm', blank=True, null=True)

    # power_supply_unit_location = models.CharField(max_length=10)
    # number_of_5_25_bays = models.PositiveIntegerField()
    # number_of_3_5_internal_bays = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} case for {self.compatible_board_form_factor} motherboards, {' x '.join([i + 'cm' for i in self.dimensions.split('x')])}"


class PowerSupplyUnit(BaseModel):
    STANDARD_CHOICES = [
        ('80 PLUS', '80 PLUS'),
        ('80 PLUS Bronze', '80 PLUS Bronze'),
        ('80 PLUS Silver', '80 PLUS Silver'),
        ('80 PLUS Gold', '80 PLUS Gold'),
        ('80 PLUS Platinum', '80 PLUS Platinum'),
    ]
    NOISE_LEVEL_CHOICES = [
        ('A++', '<15 dB(A)'),
        ('A+', '≥15 dB(A) & <20 dB(A)'),
        ('A', '≥20 dB(A) & <25 dB(A)'),
        ('A-', '≥25 dB(A) & <30 dB(A)'),
        ('STANDARD ++', '≥30 dB(A) & <35 dB(A)'),
        ('STANDARD +', '≥35 dB(A) & <40 dB(A)'),
        ('STANDARD', '≥40 dB(A) & <45 dB(A)'),
    ]
    FORM_FACTOR_CHOICES = [
        ('ATX', 'ATX'),
        ('SFX', 'SFX'),
        ('TFX', 'TFX'),
        ('Flex-ATX', 'Flex-ATX')
    ]
    spec_labels = [
        {'slug': 'psu_power', 'label': 'Мощность'},
        {'slug': 'efficiency', 'label': 'Стандарт эффективности'},
        {'slug': 'form_factor', 'label': 'Форм-фактор'},
        {'slug': 'noise_level', 'label': 'Уровень шума'}
    ]

    psu_power = models.PositiveIntegerField()
    efficiency = models.CharField(max_length=16, choices=STANDARD_CHOICES)
    form_factor = models.CharField(max_length=50, choices=FORM_FACTOR_CHOICES)
    noise_level = models.CharField(max_length=20, choices=NOISE_LEVEL_CHOICES, default='A++')

    # power_connectors = models.CharField(max_length=20)
    # pci_e_connectors = models.PositiveIntegerField()
    # molex_connectors = models.PositiveIntegerField()
    # sata_connectors = models.PositiveIntegerField()
    # adjustable_fan_speed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.psu_power}W, {self.efficiency}, {self.noise_level})"


class RAM(BaseModel):
    MEMORY_TYPE_CHOICES = [
        ('DDR', 'DDR'),
        ('DDR2', 'DDR2'),
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
    ]
    spec_labels = [
        {'slug': 'memory_type', 'label': 'Тип памяти'},
        {'slug': 'memory_capacity', 'label': 'Объем памяти'},
        {'slug': 'memory_clock_speed', 'label': 'Частота памяти'},
    ]
    memory_type = models.CharField(max_length=4, choices=MEMORY_TYPE_CHOICES)
    memory_capacity = models.PositiveIntegerField(help_text='in GB')
    memory_clock_speed = models.PositiveIntegerField(help_text='in Mhz')

    # supply_voltage = models.DecimalField(max_digits=3, decimal_places=1)
    # timings = models.CharField(max_length=5)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.memory_capacity}GB {self.memory_type} RAM ({self.memory_clock_speed}MHz)"


class GPU(BaseModel):
    CHIPSET_MODEL_CHOICES = [
        ('GTX1050Ti', 'GTX1050Ti'),
        ('GTX1060', 'GTX1060'),
        ('GTX1070', 'GTX1070'),
        ('GTX1080', 'GTX1080'),
        ('RTX2060', 'RTX2060'),
        ('RTX2070', 'RTX2070'),
        ('RTX2080', 'RTX2080'),
        ('RTX3060', 'RTX3060'),
        ('RTX3070', 'RTX3070'),
        ('RTX3080', 'RTX3080'),
        ('RTX4070', 'RTX4070'),
    ]

    MEMORY_TYPE_CHOICES = [
        ('GDDR5', 'GDDR5'),
        ('GDDR5X', 'GDDR5X'),
        ('GDDR6', 'GDDR6'),
        ('GDDR6X', 'GDDR6X')
    ]

    INTERFACE_CHOICES = [
        ('PCIe 3.0', 'PCIe 3.0'),
        ('PCIe 4.0', 'PCIe 4.0'),
        ('AGP', 'AGP'),
    ]
    spec_labels = [
        {'slug': 'interface', 'label': 'Интерфейс'},
        {'slug': 'video_memory_capacity', 'label': 'Объем видеопамяти'},
        {'slug': 'rated_power', 'label': 'Мощность'},
        {'slug': 'video_memory_type', 'label': 'Тип видеопамяти'},
        {'slug': 'technical_process', 'label': 'Технический процесс'},
        {'slug': 'gpu_frequency', 'label': 'Частота GPU'},
        {'slug': 'chipset_model', 'label': 'Модель'},
        {'slug': 'connectors', 'label': 'Коннекторы'},
        {'slug': 'length', 'label': 'Длина'},
    ]

    interface = models.CharField(max_length=20, choices=INTERFACE_CHOICES)
    video_memory_capacity = models.PositiveIntegerField()
    rated_power = models.PositiveIntegerField(help_text='in W')
    video_memory_type = models.CharField(max_length=6, choices=MEMORY_TYPE_CHOICES)
    technical_process = models.PositiveIntegerField(help_text='in nm', default=8)
    gpu_frequency = models.DecimalField(max_digits=6, decimal_places=0)
    chipset_model = models.CharField(max_length=10, choices=CHIPSET_MODEL_CHOICES)
    connectors = models.CharField(max_length=50)
    length = models.PositiveIntegerField(help_text='in mm')

    # number_of_universal_processors = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.chipset_model} {self.video_memory_capacity}GB ({self.video_memory_type}, {self.gpu_frequency} MHz, technical process - {self.technical_process}nm, connectors: {self.connectors})"


class Motherboard(BaseModel):
    FORM_FACTOR_CHOICES = [
        ('E-ATX', 'E-ATX for FullTower (305mm x 330mm)'),
        ('ATX', 'ATX for MidiTower (244mm x 305mm)'),
        ('Micro-ATX', 'Micro-ATX for MiniTower (244mm x 244mm)'),
    ]

    spec_labels = [
        {'slug': 'socket', 'label': 'Сокет'},
        {'slug': 'form_factor', 'label': 'Форм-фактор'},
        {'slug': 'num_memory_slots', 'label': 'Количество слотов памяти'},
        {'slug': 'power_connectors', 'label': 'Количество коннектеров мощности'},
    ]

    socket = models.ForeignKey(Socket, on_delete=models.RESTRICT)
    form_factor = models.CharField(max_length=40, choices=FORM_FACTOR_CHOICES)
    num_memory_slots = models.IntegerField(default=4)
    # num_pci_express_slots_x1 = models.IntegerField()
    # num_pci_express_slots_x16 = models.IntegerField()
    power_connectors = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.socket}) + {self.form_factor}"


class CPU(BaseModel):
    PROCESSOR_TYPE_CHOICES = (
        ('Celeron', 'Celeron'),
        ('Core i3', 'Core i3'),
        ('Core i5', 'Core i5'),
        ('Core i7', 'Core i7'),
        ('Core i9', 'Core i9'),
        ('Pentium', 'Pentium'),
        ('Xeon', 'Xeon'),
    )

    spec_labels = [
        {'slug': 'socket', 'label': 'Сокет'},
        {'slug': 'processor_type', 'label': 'Тип процессора'},
        {'slug': 'total_number_of_cores', 'label': 'Количество ядер'},
        {'slug': 'total_number_of_threads', 'label': 'Количество потоков'},
        {'slug': 'clock_frequency', 'label': 'Частота ядра'},
        {'slug': 'process_technology', 'label': 'Тех-процесс'},
        {'slug': 'rated_power', 'label': 'Мощность'},
    ]

    socket = models.ForeignKey(Socket, on_delete=models.RESTRICT)
    processor_type = models.CharField(max_length=10, choices=PROCESSOR_TYPE_CHOICES)
    total_number_of_cores = models.PositiveIntegerField()
    total_number_of_threads = models.PositiveIntegerField()
    clock_frequency = models.FloatField(help_text='in MHz')
    process_technology = models.PositiveIntegerField(help_text='in nm')
    rated_power = models.PositiveIntegerField(help_text='in W')

    # microarchitecture = models.CharField(max_length=10)
    # l3_cache_size = models.PositiveIntegerField(help_text='in MB')
    # integrated_graphics_system = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.processor_type} {self.total_number_of_cores} cores and {self.total_number_of_threads} threads ({self.socket})"


class Memory(BaseModel):
    HDD, SSD = 'HDD', 'SSD'

    MEMORY_TYPE_CHOICES = [
        ('HDD', 'HDD'),
        ('SSD', 'SSD'),
    ]

    memory_type = models.CharField(
        max_length=3,
        choices=MEMORY_TYPE_CHOICES,
        default=SSD,
    )
    FORM_FACTOR_CHOICES = [
        ('2.5', '2.5 inch'),
        ('M2', 'M.2'),
        ('mSATA', 'mSATA'),
        ('U2', 'U.2')
    ]
    spec_labels = [
        {'slug': 'interface', 'label': 'Интерфейс'},
        {'slug': 'form_factor', 'label': 'Форм-фактор'},
        {'slug': 'disk_capacity', 'label': 'Объем памяти'},
        {'slug': 'read_speed', 'label': 'Скорость чтения'},
        {'slug': 'write_speed', 'label': 'Скорость записи'},
    ]

    interface = models.CharField(max_length=20)
    form_factor = models.CharField(max_length=20)
    disk_capacity = models.IntegerField(help_text='in GB')
    read_speed = models.FloatField(help_text='in mb/s')
    write_speed = models.FloatField(help_text='in mb/s')

    # interface_transfer_rate = models.FloatField()

    def __str__(self):
        return f"{self.disk_capacity} GB {self.memory_type} ({self.interface} read:{self.read_speed} Gbit/s)"


# ACCESSORY


class Mouse(models.Model):
    type = models.CharField(max_length=50, choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')])
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Keyboard(models.Model):
    type = models.CharField(max_length=50, choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')])
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Monitor(models.Model):
    resolution = models.CharField(max_length=50)
    refresh_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Microphone(models.Model):
    name = models.CharField(max_length=255)
    type_choices = (
        ('wired', 'Wired'),
        ('wireless', 'Wireless')
    )
    type = models.CharField(max_length=10, choices=type_choices)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Headset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Accessory(BaseModel):
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE, null=True)
    keybord = models.ForeignKey(Keyboard, on_delete=models.CASCADE, null=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, null=True)
    microphone = models.ForeignKey(Microphone, on_delete=models.CASCADE, null=True)
    headset = models.ForeignKey(Headset, on_delete=models.CASCADE, null=True)


class Modification(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, default='')
    author_name = models.CharField(max_length=255, blank=True)
    likes = models.PositiveIntegerField(default=0)

    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    power_supply = models.ForeignKey(PowerSupplyUnit, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE)

    # accessories = models.ManyToManyField(Accessory)

    def is_compatible_cooling(self):
        return self.motherboard.socket in self.cooling.sockets.all()

    def is_compatible(self):
        return self.cpu.socket == self.motherboard.socket

    def __str__(self):
        return f"{self.name} {self.housing} {self.cpu} {self.gpu} {self.memory}"
