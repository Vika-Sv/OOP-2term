import time, statistics, random
from array import Array


RUNS = 3
N = 100
sizes = [N, N**2, N**3]   


def measure(method_name, fill, size):
    times = []
    for _ in range(RUNS):
        arr = Array(size, fill)          
        t0  = time.perf_counter_ns()
        getattr(arr, method_name)()      
        times.append(time.perf_counter_ns() - t0)
    return statistics.mean(times)


print("=" * 62)
print("ЗАВДАННЯ 1 — Низхідне злиття (Merge Sort DESC)")
print("=" * 62)
res_t1 = {}
for sz in sizes:
    t = measure("merge_sort_desc", "random", sz)
    res_t1[sz] = t
    print(f"  N = {sz:>9}  →  {t:>16.0f} нс  ({t/1e6:>10.3f} мс)")



print()
print("=" * 62)
print("ЗАВДАННЯ 2 — Злиття vs Бульбашка (однакові дані)")
print("=" * 62)
res_merge2, res_bubble2 = {}, {}
for sz in sizes:
    SEED = 42
    random.seed(SEED)
    tm = measure("merge_sort_desc", "random", sz)
    random.seed(SEED)
    tb = measure("bubble_sort",     "random", sz)
    res_merge2[sz]  = tm
    res_bubble2[sz] = tb
    print(f"  N={sz:>9} | Злиття: {tm:>14.0f} нс | Бульбашка: {tb:>14.0f} нс")


SZ3 = 10_000
print()
print("=" * 62)
print(f"ЗАВДАННЯ 3 — Послідовності ({SZ3} елементів)")
print("=" * 62)

tm_best  = measure("merge_sort_desc", "reversed", SZ3)
tm_avg   = measure("merge_sort_desc", "random",   SZ3)
tm_worst = measure("merge_sort_desc", "sorted",   SZ3)

tb_best  = measure("bubble_sort", "sorted",       SZ3)
tb_avg   = measure("bubble_sort", "random",       SZ3)
tb_worst = measure("bubble_sort", "worst_bubble", SZ3)

print("\n  Злиття (низхідне):")
print(f"    Найкращий  (відсортований ↓): {tm_best:>16.0f} нс")
print(f"    Середній   (випадковий):      {tm_avg:>16.0f} нс")
print(f"    Найгірший  (відсортований ↑): {tm_worst:>16.0f} нс")
print("\n  Бульбашка:")
print(f"    Найкращий  (відсортований ↑): {tb_best:>16.0f} нс")
print(f"    Середній   (випадковий):      {tb_avg:>16.0f} нс")
print(f"    Найгірший  (зворотній ↓):     {tb_worst:>16.0f} нс")
