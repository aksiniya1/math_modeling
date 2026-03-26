import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Polygon, RegularPolygon
import matplotlib.transforms as transforms

# ============================================
# НАСТРОЙКА ПАРАМЕТРОВ
# ============================================
ANGLE = 10 # Угол наклона рогатки в градусах
RUBBER_BAND_STRENGTH = 50  # Сила выстрела (начальная скорость)
STONE_MASS = 1.0  # Масса камня
GLASS_THICKNESS = 0.8  # Толщина стекла (прочность лампы)
LAMP_RADIUS = 2.0  # Радиус лампы

# Физические константы
GRAVITY = 5.0  # Гравитация (уменьшил для красивой анимации)
TIME_STEP = 0.05  # Шаг времени

# ============================================
# ИНИЦИАЛИЗАЦИЯ ДАННЫХ
# ============================================
# Начальная позиция камня (рогатка)
stone_start_x = -8
stone_start_y = 1.5

# Позиция лампы
lamp_x, lamp_y = 5, 1.5

# Состояние объектов
stone_pos = np.array([stone_start_x, stone_start_y])
stone_vel = np.array([
    RUBBER_BAND_STRENGTH * np.cos(np.radians(ANGLE)) / STONE_MASS,
    RUBBER_BAND_STRENGTH * np.sin(np.radians(ANGLE)) / STONE_MASS
])
stone_active = False  # Камень еще не выпущен

lamp_intact = True  # Лампа цела
fragments = []  # Осколки

# Для отслеживания выстрела
shot_fired = False

# ============================================
# НАСТРОЙКА ГРАФИКА
# ============================================
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(-10, 15)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# Рисуем землю
ax.axhline(y=0, color='brown', linewidth=3)

# ============================================
# ФУНКЦИИ ДЛЯ ОТРИСОВКИ ОБЪЕКТОВ
# ============================================
def draw_slingshot(ax, angle_deg, stone_pos_draw):
    """Рисует рогатку под заданным углом"""
    angle_rad = np.radians(angle_deg)
    
    # Основание рогатки (палка)
    ax.plot([-9, -7], [1, 3], color='saddlebrown', linewidth=4)
    ax.plot([-9, -11], [1, 3], color='saddlebrown', linewidth=4)
    ax.plot([-10, -8], [0.5, 1.5], color='saddlebrown', linewidth=3)
    
    # Резинки (рисуем только если камень еще в рогатке или не выпущен)
    if not stone_active and not shot_fired:
        # Резинка от левого рога
        ax.plot([-11, stone_pos_draw[0]], [3, stone_pos_draw[1]], 
                color='red', linewidth=2, linestyle='--', alpha=0.7)
        # Резинка от правого рога
        ax.plot([-7, stone_pos_draw[0]], [3, stone_pos_draw[1]], 
                color='red', linewidth=2, linestyle='--', alpha=0.7)

def draw_lamp(ax, x, y, radius, intact, thickness):
    """Рисует лампу (целую или разбитую)"""
    if intact:
        # Целая лампа - круг с ободком
        lamp = Circle((x, y), radius, color='yellow', alpha=0.3, ec='black', linewidth=2)
        ax.add_patch(lamp)
        # Внутренность (толщина стекла)
        inner_lamp = Circle((x, y), radius * 0.7, color='lightyellow', alpha=0.5, ec='gray', linewidth=1)
        ax.add_patch(inner_lamp)
        # Свет внутри
        filament = Circle((x, y-0.2), 0.2, color='orange', alpha=0.8)
        ax.add_patch(filament)
    else:
        # Разбитая лампа не рисуется, рисуются осколки
        pass

def draw_fragments(ax, fragments_list):
    """Рисует осколки разбитой лампы"""
    for frag in fragments_list:
        # Осколки - маленькие треугольники
        fragment = RegularPolygon(
            (frag['x'], frag['y']), 
            numVertices=3, 
            radius=0.2, 
            orientation=frag['rot'],
            color='white', 
            ec='gray', 
            alpha=0.8
        )
        ax.add_patch(fragment)

# ============================================
# ФУНКЦИЯ ОБНОВЛЕНИЯ АНИМАЦИИ
# ============================================
def update(frame):
    global stone_pos, stone_vel, stone_active, lamp_intact, fragments, shot_fired
    
    # Очищаем оси
    ax.clear()
    ax.set_xlim(-10, 15)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='brown', linewidth=3)
# Рисуем рогатку
    draw_slingshot(ax, ANGLE, stone_pos)
    
    # ===== УПРАВЛЕНИЕ ВЫСТРЕЛОМ =====
    # Автоматический выстрел через 10 кадров
    if frame == 10 and not shot_fired:
        stone_active = True
        shot_fired = True
        # Задаем скорость с учетом массы
        stone_vel = np.array([
            RUBBER_BAND_STRENGTH * np.cos(np.radians(ANGLE)) / STONE_MASS,
            RUBBER_BAND_STRENGTH * np.sin(np.radians(ANGLE)) / STONE_MASS
        ])
    
    # ===== ФИЗИКА ПОЛЕТА КАМНЯ =====
    if stone_active:
        # Гравитация
        stone_vel[1] -= GRAVITY * TIME_STEP
        
        # Обновляем позицию
        stone_pos += stone_vel * TIME_STEP
        
        # Отскок от земли
        if stone_pos[1] < 0.2:
            stone_pos[1] = 0.2
            stone_vel[1] = -stone_vel[1] * 0.5  # Потеря энергии при ударе
            stone_vel[0] *= 0.95  # Трение
        
        # Останавливаем камень если он совсем замедлился
        if np.linalg.norm(stone_vel) < 0.1 and stone_pos[1] <= 0.5:
            stone_active = False
    
    # ===== ПРОВЕРКА СТОЛКНОВЕНИЯ С ЛАМПОЙ =====
    if lamp_intact and stone_active:
        # Расстояние от камня до центра лампы
        dist = np.linalg.norm(stone_pos - np.array([lamp_x, lamp_y]))
        
        if dist < LAMP_RADIUS + 0.3:  # Столкновение
            # Рассчитываем импульс камня
            momentum = np.linalg.norm(stone_vel) * STONE_MASS
            
            # Проверяем, разбивается ли лампа
            if momentum > GLASS_THICKNESS * 30:  # Порог разрушения
                lamp_intact = False
                
                # Создаем осколки
                num_fragments = int(8 + momentum * 2)
                for i in range(num_fragments):
                    angle = np.random.uniform(0, 2*np.pi)
                    speed = np.random.uniform(2, 8) * (momentum / 50)
                    fragments.append({
                        'x': lamp_x,
                        'y': lamp_y,
                        'vx': np.cos(angle) * speed,
                        'vy': np.sin(angle) * speed,
                        'rot': np.random.uniform(0, 2*np.pi)
                    })
                
                # Камень останавливается или отлетает
                stone_vel = stone_vel * 0.2  # Сильно замедляется
                
                ax.set_title("💥 БАБАХ! Лампа разбита! 💥", fontsize=14, color='red')
            else:
                # Отскок от лампы
                # Нормаль от центра лампы к камню
                normal = (stone_pos - np.array([lamp_x, lamp_y])) / dist
                stone_vel = stone_vel - 2 * np.dot(stone_vel, normal) * normal
                stone_vel *= 0.8  # Потеря энергии
                
                # Отодвигаем камень от лампы чтобы избежать залипания
                stone_pos = np.array([lamp_x, lamp_y]) + normal * (LAMP_RADIUS + 0.4)
                
                ax.set_title("💢 Дзынь! Камень отскочил", fontsize=12, color='orange')
    
    # ===== ФИЗИКА ОСКОЛКОВ =====
    if not lamp_intact and fragments:
        # Обновляем позиции осколков
        for frag in fragments[:]:
            # Гравитация для осколков
            frag['vy'] -= GRAVITY * TIME_STEP * 0.5
            frag['x'] += frag['vx'] * TIME_STEP
            frag['y'] += frag['vy'] * TIME_STEP
            frag['rot'] += 0.1  # Вращение
            
            # Отскок от земли
            if frag['y'] < 0.1:
                frag['y'] = 0.1
                frag['vy'] = -frag['vy'] * 0.3
                frag['vx'] *= 0.8
            
            # Удаляем очень медленные осколки
            if abs(frag['vx']) < 0.1 and abs(frag['vy']) < 0.1 and frag['y'] < 0.2:
                fragments.remove(frag)
        
        # Рисуем осколки
        draw_fragments(ax, fragments)
    
    # ===== ОТРИСОВКА ОБЪЕКТОВ =====
    # Рисуем лампу
    draw_lamp(ax, lamp_x, lamp_y, LAMP_RADIUS, lamp_intact, GLASS_THICKNESS)
    
    # Рисуем камень (размер зависит от массы)
    stone_size = 0.15 + STONE_MASS * 0.1
    if stone_active or not shot_fired:
        stone = Circle(stone_pos, stone_size, color='gray', ec='black', linewidth=1)
        ax.add_patch(stone)
    
    # ===== СТАТУС В ЗАГОЛОВКЕ =====
    status = f"Угол: {ANGLE}° | Сила: {RUBBER_BAND_STRENGTH} | Масса: {STONE_MASS:.1f} | Толщина стекла: {GLASS_THICKNESS}"
    if not lamp_intact:
        ax.set_title(f"💥 РАЗБИТА! 💥 | {status}", fontsize=12)
    elif stone_active:
        ax.set_title(f"🔫 Выстрел! | {status}", fontsize=12)
    else:
        ax.set_title(f"🎯 Рогатка заряжена | {status}", fontsize=12)

# ============================================
# ЗАПУСК АНИМАЦИИ
ani = FuncAnimation(fig, update, frames=500, interval=50, repeat=False)

ani.save('animation_1.gif', writer="pillow")

