from typing import Iterator

_input_sm = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

_input_lg = """
Button A: X+26, Y+57
Button B: X+51, Y+13
Prize: X=15496, Y=17815

Button A: X+20, Y+81
Button B: X+66, Y+14
Prize: X=13062, Y=10478

Button A: X+73, Y+15
Button B: X+29, Y+42
Prize: X=7707, Y=4539

Button A: X+27, Y+49
Button B: X+57, Y+29
Prize: X=19292, Y=19334

Button A: X+72, Y+24
Button B: X+25, Y+73
Prize: X=17782, Y=9862

Button A: X+15, Y+64
Button B: X+92, Y+93
Prize: X=3982, Y=4709

Button A: X+82, Y+22
Button B: X+46, Y+99
Prize: X=6862, Y=5654

Button A: X+73, Y+17
Button B: X+47, Y+50
Prize: X=3183, Y=1991

Button A: X+35, Y+12
Button B: X+47, Y+67
Prize: X=17523, Y=7451

Button A: X+65, Y+19
Button B: X+12, Y+43
Prize: X=15587, Y=17340

Button A: X+15, Y+33
Button B: X+63, Y+20
Prize: X=18581, Y=7263

Button A: X+57, Y+93
Button B: X+82, Y+28
Prize: X=4578, Y=7152

Button A: X+96, Y+64
Button B: X+17, Y+69
Prize: X=3737, Y=6701

Button A: X+82, Y+24
Button B: X+46, Y+99
Prize: X=7390, Y=5841

Button A: X+65, Y+25
Button B: X+19, Y+58
Prize: X=12867, Y=11274

Button A: X+83, Y+46
Button B: X+46, Y+88
Prize: X=6328, Y=7820

Button A: X+22, Y+38
Button B: X+51, Y+17
Prize: X=15619, Y=1409

Button A: X+33, Y+92
Button B: X+17, Y+14
Prize: X=4069, Y=9574

Button A: X+11, Y+36
Button B: X+54, Y+37
Prize: X=13225, Y=1602

Button A: X+79, Y+32
Button B: X+18, Y+59
Prize: X=8050, Y=15135

Button A: X+42, Y+68
Button B: X+68, Y+31
Prize: X=3126, Y=2451

Button A: X+71, Y+18
Button B: X+13, Y+59
Prize: X=5318, Y=7029

Button A: X+28, Y+84
Button B: X+89, Y+23
Prize: X=3256, Y=3912

Button A: X+30, Y+68
Button B: X+65, Y+27
Prize: X=16480, Y=16024

Button A: X+35, Y+16
Button B: X+43, Y+63
Prize: X=2645, Y=1949

Button A: X+61, Y+43
Button B: X+15, Y+45
Prize: X=6334, Y=5842

Button A: X+75, Y+21
Button B: X+12, Y+59
Prize: X=5084, Y=18594

Button A: X+13, Y+46
Button B: X+64, Y+35
Prize: X=10735, Y=12326

Button A: X+18, Y+50
Button B: X+63, Y+20
Prize: X=818, Y=4410

Button A: X+70, Y+18
Button B: X+19, Y+71
Prize: X=2111, Y=5647

Button A: X+36, Y+62
Button B: X+49, Y+16
Prize: X=19024, Y=6036

Button A: X+16, Y+34
Button B: X+56, Y+24
Prize: X=5160, Y=8740

Button A: X+47, Y+90
Button B: X+87, Y+45
Prize: X=2445, Y=2250

Button A: X+41, Y+53
Button B: X+83, Y+20
Prize: X=1949, Y=599

Button A: X+84, Y+43
Button B: X+11, Y+32
Prize: X=7833, Y=5671

Button A: X+79, Y+71
Button B: X+15, Y+57
Prize: X=1240, Y=2420

Button A: X+48, Y+14
Button B: X+20, Y+74
Prize: X=18404, Y=4066

Button A: X+16, Y+39
Button B: X+45, Y+19
Prize: X=7372, Y=3455

Button A: X+75, Y+31
Button B: X+14, Y+75
Prize: X=1426, Y=4673

Button A: X+41, Y+19
Button B: X+20, Y+45
Prize: X=1495, Y=8405

Button A: X+33, Y+62
Button B: X+27, Y+12
Prize: X=10865, Y=15726

Button A: X+90, Y+80
Button B: X+27, Y+85
Prize: X=2115, Y=3405

Button A: X+56, Y+12
Button B: X+67, Y+73
Prize: X=5374, Y=5022

Button A: X+23, Y+71
Button B: X+65, Y+15
Prize: X=9301, Y=1597

Button A: X+13, Y+34
Button B: X+78, Y+55
Prize: X=11261, Y=4722

Button A: X+25, Y+13
Button B: X+35, Y+84
Prize: X=2565, Y=4558

Button A: X+70, Y+31
Button B: X+20, Y+62
Prize: X=11690, Y=6749

Button A: X+71, Y+26
Button B: X+33, Y+65
Prize: X=5473, Y=3380

Button A: X+29, Y+74
Button B: X+57, Y+23
Prize: X=4321, Y=7475

Button A: X+32, Y+69
Button B: X+58, Y+32
Prize: X=4332, Y=5060

Button A: X+99, Y+12
Button B: X+37, Y+43
Prize: X=4776, Y=810

Button A: X+14, Y+41
Button B: X+67, Y+19
Prize: X=4835, Y=3704

Button A: X+41, Y+99
Button B: X+59, Y+40
Prize: X=2266, Y=4242

Button A: X+96, Y+41
Button B: X+27, Y+93
Prize: X=8178, Y=7892

Button A: X+21, Y+59
Button B: X+66, Y+19
Prize: X=6632, Y=13403

Button A: X+57, Y+27
Button B: X+11, Y+31
Prize: X=2568, Y=8668

Button A: X+78, Y+15
Button B: X+11, Y+76
Prize: X=1828, Y=13755

Button A: X+81, Y+31
Button B: X+12, Y+46
Prize: X=15002, Y=3378

Button A: X+79, Y+13
Button B: X+18, Y+76
Prize: X=5203, Y=11361

Button A: X+39, Y+60
Button B: X+42, Y+12
Prize: X=9614, Y=1508

Button A: X+89, Y+13
Button B: X+84, Y+87
Prize: X=10089, Y=4986

Button A: X+33, Y+76
Button B: X+95, Y+51
Prize: X=10102, Y=6822

Button A: X+25, Y+65
Button B: X+60, Y+18
Prize: X=10890, Y=8512

Button A: X+29, Y+11
Button B: X+12, Y+19
Prize: X=7479, Y=9810

Button A: X+97, Y+15
Button B: X+76, Y+62
Prize: X=9745, Y=5577

Button A: X+19, Y+52
Button B: X+72, Y+31
Prize: X=7974, Y=612

Button A: X+96, Y+60
Button B: X+28, Y+85
Prize: X=6896, Y=10520

Button A: X+57, Y+29
Button B: X+14, Y+29
Prize: X=14115, Y=15866

Button A: X+85, Y+13
Button B: X+48, Y+84
Prize: X=4201, Y=2329

Button A: X+11, Y+48
Button B: X+27, Y+12
Prize: X=18447, Y=10292

Button A: X+40, Y+15
Button B: X+24, Y+62
Prize: X=9368, Y=15709

Button A: X+32, Y+11
Button B: X+46, Y+65
Prize: X=7678, Y=17148

Button A: X+73, Y+72
Button B: X+78, Y+12
Prize: X=4009, Y=2136

Button A: X+27, Y+53
Button B: X+58, Y+35
Prize: X=15696, Y=13514

Button A: X+79, Y+34
Button B: X+31, Y+79
Prize: X=2648, Y=3569

Button A: X+12, Y+60
Button B: X+74, Y+32
Prize: X=14124, Y=8520

Button A: X+28, Y+66
Button B: X+92, Y+32
Prize: X=9444, Y=7842

Button A: X+57, Y+27
Button B: X+29, Y+66
Prize: X=9346, Y=6842

Button A: X+13, Y+76
Button B: X+51, Y+53
Prize: X=1091, Y=2946

Button A: X+62, Y+23
Button B: X+27, Y+59
Prize: X=15707, Y=18535

Button A: X+65, Y+12
Button B: X+87, Y+84
Prize: X=9096, Y=5280

Button A: X+60, Y+73
Button B: X+81, Y+12
Prize: X=13554, Y=8355

Button A: X+13, Y+90
Button B: X+94, Y+21
Prize: X=8504, Y=6603

Button A: X+98, Y+39
Button B: X+53, Y+73
Prize: X=6044, Y=7077

Button A: X+71, Y+11
Button B: X+24, Y+84
Prize: X=15342, Y=14922

Button A: X+32, Y+14
Button B: X+38, Y+55
Prize: X=6166, Y=3033

Button A: X+45, Y+17
Button B: X+24, Y+50
Prize: X=14639, Y=15983

Button A: X+28, Y+85
Button B: X+70, Y+43
Prize: X=3192, Y=7656

Button A: X+19, Y+87
Button B: X+42, Y+35
Prize: X=2071, Y=6494

Button A: X+95, Y+71
Button B: X+32, Y+82
Prize: X=4128, Y=5060

Button A: X+38, Y+16
Button B: X+33, Y+61
Prize: X=8304, Y=16358

Button A: X+82, Y+41
Button B: X+15, Y+55
Prize: X=2817, Y=4876

Button A: X+13, Y+52
Button B: X+84, Y+46
Prize: X=18258, Y=17082

Button A: X+77, Y+56
Button B: X+27, Y+65
Prize: X=7985, Y=9391

Button A: X+19, Y+63
Button B: X+95, Y+36
Prize: X=9101, Y=7578

Button A: X+53, Y+26
Button B: X+11, Y+21
Prize: X=4919, Y=4544

Button A: X+26, Y+72
Button B: X+39, Y+27
Prize: X=5070, Y=7560

Button A: X+14, Y+26
Button B: X+61, Y+36
Prize: X=5189, Y=4304

Button A: X+49, Y+13
Button B: X+42, Y+48
Prize: X=6678, Y=4536

Button A: X+86, Y+39
Button B: X+12, Y+55
Prize: X=9306, Y=6676

Button A: X+21, Y+99
Button B: X+53, Y+44
Prize: X=1975, Y=4576

Button A: X+29, Y+47
Button B: X+46, Y+14
Prize: X=2373, Y=323

Button A: X+33, Y+51
Button B: X+33, Y+16
Prize: X=3861, Y=4042

Button A: X+16, Y+35
Button B: X+56, Y+29
Prize: X=12328, Y=15241

Button A: X+79, Y+46
Button B: X+42, Y+96
Prize: X=9137, Y=11330

Button A: X+33, Y+18
Button B: X+24, Y+44
Prize: X=1907, Y=17842

Button A: X+36, Y+65
Button B: X+53, Y+17
Prize: X=7394, Y=10972

Button A: X+13, Y+40
Button B: X+49, Y+19
Prize: X=16980, Y=18282

Button A: X+12, Y+32
Button B: X+54, Y+35
Prize: X=15608, Y=17942

Button A: X+19, Y+96
Button B: X+90, Y+28
Prize: X=5195, Y=7472

Button A: X+79, Y+20
Button B: X+11, Y+52
Prize: X=1308, Y=4416

Button A: X+70, Y+43
Button B: X+13, Y+33
Prize: X=2728, Y=16318

Button A: X+27, Y+57
Button B: X+69, Y+35
Prize: X=19667, Y=16365

Button A: X+61, Y+15
Button B: X+23, Y+78
Prize: X=15537, Y=5324

Button A: X+15, Y+37
Button B: X+83, Y+59
Prize: X=14468, Y=18532

Button A: X+42, Y+23
Button B: X+28, Y+59
Prize: X=1810, Y=3395

Button A: X+82, Y+14
Button B: X+15, Y+74
Prize: X=7375, Y=16290

Button A: X+64, Y+22
Button B: X+30, Y+70
Prize: X=6200, Y=7440

Button A: X+99, Y+24
Button B: X+11, Y+12
Prize: X=2860, Y=1188

Button A: X+17, Y+39
Button B: X+69, Y+41
Prize: X=7116, Y=16904

Button A: X+99, Y+88
Button B: X+14, Y+92
Prize: X=6363, Y=6372

Button A: X+57, Y+87
Button B: X+95, Y+46
Prize: X=7410, Y=8637

Button A: X+46, Y+31
Button B: X+13, Y+36
Prize: X=14091, Y=7260

Button A: X+26, Y+54
Button B: X+60, Y+34
Prize: X=1774, Y=12646

Button A: X+49, Y+58
Button B: X+75, Y+19
Prize: X=4463, Y=3957

Button A: X+11, Y+55
Button B: X+26, Y+18
Prize: X=2948, Y=6116

Button A: X+19, Y+93
Button B: X+74, Y+22
Prize: X=6888, Y=3096

Button A: X+38, Y+72
Button B: X+63, Y+12
Prize: X=1149, Y=996

Button A: X+43, Y+79
Button B: X+54, Y+25
Prize: X=4804, Y=2815

Button A: X+15, Y+54
Button B: X+99, Y+69
Prize: X=2346, Y=2985

Button A: X+78, Y+70
Button B: X+26, Y+80
Prize: X=9360, Y=13330

Button A: X+52, Y+12
Button B: X+34, Y+67
Prize: X=13144, Y=11462

Button A: X+50, Y+19
Button B: X+53, Y+98
Prize: X=1898, Y=1967

Button A: X+46, Y+15
Button B: X+29, Y+59
Prize: X=15349, Y=1647

Button A: X+16, Y+71
Button B: X+69, Y+12
Prize: X=14848, Y=3054

Button A: X+70, Y+16
Button B: X+14, Y+47
Prize: X=15544, Y=7609

Button A: X+66, Y+22
Button B: X+62, Y+76
Prize: X=7270, Y=6850

Button A: X+19, Y+75
Button B: X+34, Y+26
Prize: X=2697, Y=3937

Button A: X+62, Y+39
Button B: X+17, Y+47
Prize: X=6349, Y=8658

Button A: X+11, Y+46
Button B: X+64, Y+13
Prize: X=17366, Y=18904

Button A: X+17, Y+58
Button B: X+27, Y+13
Prize: X=593, Y=15287

Button A: X+39, Y+60
Button B: X+86, Y+25
Prize: X=4635, Y=1980

Button A: X+22, Y+57
Button B: X+93, Y+74
Prize: X=2326, Y=4023

Button A: X+80, Y+39
Button B: X+15, Y+48
Prize: X=16720, Y=2783

Button A: X+98, Y+94
Button B: X+79, Y+15
Prize: X=4327, Y=2631

Button A: X+57, Y+73
Button B: X+68, Y+26
Prize: X=9634, Y=7268

Button A: X+29, Y+19
Button B: X+13, Y+28
Prize: X=8784, Y=14474

Button A: X+19, Y+32
Button B: X+48, Y+13
Prize: X=14507, Y=18875

Button A: X+32, Y+86
Button B: X+62, Y+14
Prize: X=4008, Y=6498

Button A: X+36, Y+95
Button B: X+64, Y+11
Prize: X=5176, Y=4975

Button A: X+31, Y+58
Button B: X+42, Y+16
Prize: X=2690, Y=4720

Button A: X+74, Y+82
Button B: X+91, Y+14
Prize: X=12547, Y=8780

Button A: X+44, Y+12
Button B: X+35, Y+62
Prize: X=18163, Y=16198

Button A: X+77, Y+31
Button B: X+14, Y+43
Prize: X=3612, Y=2874

Button A: X+88, Y+98
Button B: X+85, Y+13
Prize: X=3940, Y=1448

Button A: X+54, Y+96
Button B: X+55, Y+20
Prize: X=5777, Y=6148

Button A: X+39, Y+11
Button B: X+15, Y+32
Prize: X=3450, Y=3389

Button A: X+58, Y+23
Button B: X+36, Y+71
Prize: X=5670, Y=3780

Button A: X+29, Y+11
Button B: X+39, Y+64
Prize: X=5057, Y=10830

Button A: X+69, Y+74
Button B: X+98, Y+14
Prize: X=10935, Y=5988

Button A: X+33, Y+82
Button B: X+91, Y+18
Prize: X=3018, Y=1880

Button A: X+14, Y+66
Button B: X+68, Y+15
Prize: X=8874, Y=14402

Button A: X+16, Y+70
Button B: X+39, Y+19
Prize: X=1802, Y=6974

Button A: X+67, Y+43
Button B: X+12, Y+26
Prize: X=6577, Y=16569

Button A: X+11, Y+26
Button B: X+70, Y+46
Prize: X=11514, Y=2076

Button A: X+21, Y+45
Button B: X+35, Y+13
Prize: X=12583, Y=5637

Button A: X+56, Y+14
Button B: X+27, Y+70
Prize: X=3749, Y=9804

Button A: X+78, Y+15
Button B: X+15, Y+62
Prize: X=9104, Y=17334

Button A: X+28, Y+48
Button B: X+56, Y+28
Prize: X=13080, Y=7784

Button A: X+65, Y+32
Button B: X+12, Y+40
Prize: X=8025, Y=19496

Button A: X+14, Y+57
Button B: X+57, Y+11
Prize: X=5524, Y=7392

Button A: X+16, Y+87
Button B: X+33, Y+11
Prize: X=1574, Y=2158

Button A: X+34, Y+15
Button B: X+12, Y+44
Prize: X=6952, Y=3878

Button A: X+97, Y+37
Button B: X+31, Y+75
Prize: X=3699, Y=5391

Button A: X+11, Y+65
Button B: X+75, Y+25
Prize: X=4631, Y=10565

Button A: X+55, Y+17
Button B: X+59, Y+98
Prize: X=4568, Y=4762

Button A: X+15, Y+48
Button B: X+76, Y+37
Prize: X=1708, Y=9547

Button A: X+73, Y+25
Button B: X+19, Y+58
Prize: X=14528, Y=8489

Button A: X+41, Y+79
Button B: X+53, Y+15
Prize: X=183, Y=13369

Button A: X+20, Y+66
Button B: X+61, Y+14
Prize: X=16112, Y=11130

Button A: X+48, Y+17
Button B: X+16, Y+37
Prize: X=8320, Y=17122

Button A: X+88, Y+29
Button B: X+49, Y+99
Prize: X=10732, Y=7845

Button A: X+39, Y+74
Button B: X+57, Y+20
Prize: X=4013, Y=15344

Button A: X+91, Y+71
Button B: X+17, Y+97
Prize: X=7772, Y=9832

Button A: X+34, Y+72
Button B: X+58, Y+19
Prize: X=14216, Y=18213

Button A: X+86, Y+16
Button B: X+13, Y+86
Prize: X=3054, Y=1404

Button A: X+26, Y+72
Button B: X+44, Y+12
Prize: X=8224, Y=18524

Button A: X+28, Y+64
Button B: X+41, Y+13
Prize: X=18355, Y=6055

Button A: X+16, Y+46
Button B: X+73, Y+34
Prize: X=1805, Y=11054

Button A: X+14, Y+40
Button B: X+53, Y+11
Prize: X=15743, Y=14999

Button A: X+80, Y+56
Button B: X+11, Y+28
Prize: X=3022, Y=704

Button A: X+12, Y+70
Button B: X+56, Y+15
Prize: X=3404, Y=13855

Button A: X+32, Y+67
Button B: X+49, Y+22
Prize: X=12592, Y=14397

Button A: X+78, Y+54
Button B: X+18, Y+41
Prize: X=13664, Y=18184

Button A: X+36, Y+84
Button B: X+61, Y+15
Prize: X=9920, Y=13064

Button A: X+29, Y+29
Button B: X+12, Y+92
Prize: X=1367, Y=6807

Button A: X+48, Y+18
Button B: X+31, Y+54
Prize: X=1204, Y=19574

Button A: X+12, Y+88
Button B: X+94, Y+71
Prize: X=1054, Y=3401

Button A: X+46, Y+21
Button B: X+24, Y+62
Prize: X=19754, Y=3171

Button A: X+25, Y+97
Button B: X+55, Y+49
Prize: X=3030, Y=6660

Button A: X+33, Y+65
Button B: X+49, Y+12
Prize: X=10709, Y=952

Button A: X+70, Y+34
Button B: X+17, Y+53
Prize: X=9785, Y=10541

Button A: X+19, Y+75
Button B: X+87, Y+69
Prize: X=5252, Y=5364

Button A: X+35, Y+58
Button B: X+32, Y+15
Prize: X=8591, Y=12501

Button A: X+58, Y+72
Button B: X+85, Y+19
Prize: X=3912, Y=3472

Button A: X+67, Y+11
Button B: X+35, Y+60
Prize: X=2581, Y=4113

Button A: X+96, Y+11
Button B: X+14, Y+61
Prize: X=2434, Y=1645

Button A: X+86, Y+17
Button B: X+36, Y+40
Prize: X=6750, Y=3965

Button A: X+12, Y+35
Button B: X+50, Y+11
Prize: X=14072, Y=1276

Button A: X+14, Y+65
Button B: X+97, Y+55
Prize: X=8508, Y=10245

Button A: X+57, Y+16
Button B: X+24, Y+53
Prize: X=17963, Y=1031

Button A: X+13, Y+37
Button B: X+43, Y+18
Prize: X=6253, Y=3317

Button A: X+18, Y+78
Button B: X+68, Y+14
Prize: X=5802, Y=4092

Button A: X+24, Y+56
Button B: X+74, Y+40
Prize: X=8946, Y=4664

Button A: X+16, Y+52
Button B: X+62, Y+32
Prize: X=16852, Y=2200

Button A: X+16, Y+50
Button B: X+53, Y+40
Prize: X=6069, Y=6780

Button A: X+18, Y+90
Button B: X+53, Y+56
Prize: X=1398, Y=1974

Button A: X+77, Y+82
Button B: X+15, Y+79
Prize: X=5495, Y=6293

Button A: X+41, Y+14
Button B: X+18, Y+68
Prize: X=9063, Y=8562

Button A: X+15, Y+85
Button B: X+90, Y+73
Prize: X=9675, Y=11999

Button A: X+14, Y+74
Button B: X+51, Y+17
Prize: X=3190, Y=4738

Button A: X+17, Y+30
Button B: X+83, Y+37
Prize: X=3248, Y=2995

Button A: X+83, Y+42
Button B: X+19, Y+81
Prize: X=5106, Y=3369

Button A: X+19, Y+41
Button B: X+44, Y+21
Prize: X=18698, Y=10787

Button A: X+19, Y+58
Button B: X+61, Y+11
Prize: X=2384, Y=15930

Button A: X+73, Y+52
Button B: X+12, Y+35
Prize: X=8171, Y=9895

Button A: X+86, Y+97
Button B: X+11, Y+55
Prize: X=4085, Y=6439

Button A: X+64, Y+24
Button B: X+14, Y+57
Prize: X=14120, Y=332

Button A: X+89, Y+17
Button B: X+62, Y+73
Prize: X=2030, Y=2039

Button A: X+97, Y+50
Button B: X+31, Y+58
Prize: X=6088, Y=6920

Button A: X+94, Y+11
Button B: X+23, Y+76
Prize: X=3784, Y=3815

Button A: X+74, Y+12
Button B: X+14, Y+36
Prize: X=2332, Y=1896

Button A: X+35, Y+14
Button B: X+32, Y+47
Prize: X=1423, Y=1903

Button A: X+22, Y+52
Button B: X+73, Y+37
Prize: X=15481, Y=1537

Button A: X+11, Y+36
Button B: X+53, Y+19
Prize: X=666, Y=944

Button A: X+25, Y+54
Button B: X+58, Y+24
Prize: X=11466, Y=18980

Button A: X+17, Y+27
Button B: X+36, Y+17
Prize: X=1897, Y=12407

Button A: X+79, Y+40
Button B: X+27, Y+73
Prize: X=4741, Y=4833

Button A: X+41, Y+69
Button B: X+37, Y+14
Prize: X=15015, Y=9450

Button A: X+60, Y+33
Button B: X+35, Y+59
Prize: X=10025, Y=314

Button A: X+17, Y+36
Button B: X+55, Y+13
Prize: X=11301, Y=15168

Button A: X+96, Y+65
Button B: X+36, Y+96
Prize: X=4764, Y=3727

Button A: X+11, Y+57
Button B: X+74, Y+30
Prize: X=3734, Y=6146

Button A: X+55, Y+13
Button B: X+23, Y+77
Prize: X=4431, Y=9909

Button A: X+48, Y+17
Button B: X+54, Y+87
Prize: X=8184, Y=8057

Button A: X+67, Y+63
Button B: X+75, Y+16
Prize: X=7827, Y=5615

Button A: X+13, Y+63
Button B: X+73, Y+22
Prize: X=13874, Y=4796

Button A: X+61, Y+28
Button B: X+11, Y+40
Prize: X=1316, Y=5424

Button A: X+46, Y+74
Button B: X+88, Y+46
Prize: X=4688, Y=5248

Button A: X+31, Y+73
Button B: X+45, Y+29
Prize: X=1389, Y=2963

Button A: X+75, Y+22
Button B: X+13, Y+52
Prize: X=16116, Y=16300

Button A: X+54, Y+29
Button B: X+14, Y+53
Prize: X=3490, Y=6303

Button A: X+92, Y+40
Button B: X+61, Y+98
Prize: X=9054, Y=8940

Button A: X+40, Y+17
Button B: X+26, Y+67
Prize: X=1846, Y=13017

Button A: X+65, Y+37
Button B: X+14, Y+99
Prize: X=7303, Y=9801

Button A: X+55, Y+28
Button B: X+24, Y+50
Prize: X=786, Y=10508

Button A: X+12, Y+48
Button B: X+81, Y+26
Prize: X=3537, Y=4314

Button A: X+29, Y+70
Button B: X+68, Y+32
Prize: X=4657, Y=4502

Button A: X+22, Y+61
Button B: X+60, Y+24
Prize: X=7344, Y=7968

Button A: X+75, Y+41
Button B: X+11, Y+51
Prize: X=11493, Y=5927

Button A: X+42, Y+83
Button B: X+53, Y+11
Prize: X=8493, Y=9605

Button A: X+45, Y+46
Button B: X+79, Y+20
Prize: X=5516, Y=4788

Button A: X+84, Y+16
Button B: X+84, Y+75
Prize: X=13188, Y=5993

Button A: X+11, Y+94
Button B: X+78, Y+45
Prize: X=2086, Y=6638

Button A: X+83, Y+28
Button B: X+56, Y+91
Prize: X=3610, Y=2660

Button A: X+64, Y+15
Button B: X+20, Y+68
Prize: X=11692, Y=17535

Button A: X+54, Y+24
Button B: X+24, Y+61
Prize: X=3348, Y=4659

Button A: X+27, Y+61
Button B: X+60, Y+30
Prize: X=11660, Y=1330

Button A: X+32, Y+18
Button B: X+23, Y+53
Prize: X=4882, Y=6512

Button A: X+95, Y+34
Button B: X+23, Y+30
Prize: X=11472, Y=6152

Button A: X+23, Y+48
Button B: X+62, Y+33
Prize: X=510, Y=5855

Button A: X+55, Y+42
Button B: X+12, Y+54
Prize: X=2205, Y=1908

Button A: X+18, Y+11
Button B: X+12, Y+38
Prize: X=7958, Y=10693

Button A: X+11, Y+61
Button B: X+59, Y+55
Prize: X=5913, Y=9927

Button A: X+30, Y+64
Button B: X+82, Y+23
Prize: X=10452, Y=7712

Button A: X+11, Y+60
Button B: X+70, Y+31
Prize: X=7395, Y=3976

Button A: X+30, Y+80
Button B: X+61, Y+17
Prize: X=7588, Y=7416

Button A: X+56, Y+22
Button B: X+26, Y+57
Prize: X=18250, Y=6355

Button A: X+49, Y+12
Button B: X+16, Y+33
Prize: X=5752, Y=4026

Button A: X+91, Y+84
Button B: X+82, Y+13
Prize: X=12139, Y=5751

Button A: X+16, Y+35
Button B: X+72, Y+41
Prize: X=12752, Y=13927

Button A: X+24, Y+76
Button B: X+87, Y+72
Prize: X=9660, Y=11868

Button A: X+68, Y+23
Button B: X+63, Y+99
Prize: X=4948, Y=5092

Button A: X+34, Y+98
Button B: X+86, Y+72
Prize: X=3820, Y=8900

Button A: X+31, Y+62
Button B: X+42, Y+11
Prize: X=12674, Y=12271

Button A: X+29, Y+38
Button B: X+57, Y+21
Prize: X=2526, Y=1914

Button A: X+27, Y+65
Button B: X+33, Y+20
Prize: X=2022, Y=1955

Button A: X+24, Y+44
Button B: X+29, Y+16
Prize: X=19334, Y=19344

Button A: X+99, Y+60
Button B: X+37, Y+88
Prize: X=10117, Y=9148

Button A: X+34, Y+14
Button B: X+14, Y+59
Prize: X=3768, Y=18903

Button A: X+84, Y+20
Button B: X+63, Y+60
Prize: X=6258, Y=2480

Button A: X+30, Y+64
Button B: X+68, Y+34
Prize: X=17778, Y=19104

Button A: X+14, Y+85
Button B: X+39, Y+37
Prize: X=1598, Y=6106

Button A: X+92, Y+42
Button B: X+13, Y+41
Prize: X=7615, Y=5405

Button A: X+29, Y+88
Button B: X+28, Y+15
Prize: X=1819, Y=2931

Button A: X+90, Y+52
Button B: X+11, Y+86
Prize: X=2564, Y=1800

Button A: X+36, Y+16
Button B: X+23, Y+32
Prize: X=18203, Y=5056

Button A: X+19, Y+42
Button B: X+75, Y+53
Prize: X=17642, Y=9310

Button A: X+49, Y+19
Button B: X+59, Y+96
Prize: X=3116, Y=4645

Button A: X+57, Y+25
Button B: X+18, Y+98
Prize: X=2361, Y=9145

Button A: X+20, Y+60
Button B: X+22, Y+17
Prize: X=2380, Y=5670

Button A: X+11, Y+57
Button B: X+66, Y+12
Prize: X=14092, Y=6494

Button A: X+80, Y+41
Button B: X+11, Y+42
Prize: X=5376, Y=3337

Button A: X+12, Y+38
Button B: X+41, Y+17
Prize: X=4306, Y=14086

Button A: X+12, Y+31
Button B: X+67, Y+24
Prize: X=12982, Y=774

Button A: X+64, Y+95
Button B: X+69, Y+29
Prize: X=5046, Y=2938

Button A: X+18, Y+56
Button B: X+25, Y+12
Prize: X=18739, Y=1924

Button A: X+93, Y+28
Button B: X+34, Y+52
Prize: X=10246, Y=6760

Button A: X+38, Y+11
Button B: X+17, Y+26
Prize: X=6062, Y=2948

Button A: X+33, Y+18
Button B: X+14, Y+50
Prize: X=14693, Y=9410

Button A: X+80, Y+14
Button B: X+16, Y+72
Prize: X=336, Y=15754

Button A: X+87, Y+12
Button B: X+62, Y+84
Prize: X=6307, Y=4416

Button A: X+20, Y+60
Button B: X+36, Y+15
Prize: X=4732, Y=6570

Button A: X+19, Y+78
Button B: X+35, Y+18
Prize: X=4115, Y=8598

Button A: X+30, Y+44
Button B: X+96, Y+35
Prize: X=9468, Y=6163

Button A: X+71, Y+96
Button B: X+62, Y+23
Prize: X=4729, Y=5725

Button A: X+20, Y+43
Button B: X+43, Y+14
Prize: X=10829, Y=16073

Button A: X+12, Y+53
Button B: X+90, Y+47
Prize: X=6066, Y=6112

Button A: X+75, Y+20
Button B: X+56, Y+74
Prize: X=5137, Y=5918

Button A: X+22, Y+57
Button B: X+67, Y+26
Prize: X=9086, Y=311
"""

from pprint import pp  # noqa
import dataclasses  # noqa

Position = tuple[int, int]


class NoSolution(Exception):
    pass


@dataclasses.dataclass
class Machine:
    move_a: Position
    move_b: Position
    prize: Position
    cost_a: int
    cost_b: int


def parse_button(line: str) -> Position:
    xstr, ystr = line.split(": ")[1].split(", ")
    x = int(xstr.split("+")[1])
    y = int(ystr.split("+")[1])
    return x, y


def parse_prize(line: str) -> Position:
    xstr, ystr = line.split(": ")[1].split(", ")
    x = int(xstr.split("=")[1])
    y = int(ystr.split("=")[1])
    return x, y


def parse_machine(mac_str: str) -> Machine:
    move_a = move_b = prize = None
    cost_a = 3
    cost_b = 1

    for line in mac_str.split("\n"):
        if line.startswith("Button A:"):
            move_a = parse_button(line)
        elif line.startswith("Button B:"):
            move_b = parse_button(line)
        elif line.startswith("Prize:"):
            prize = parse_prize(line)

    return Machine(move_a, move_b, prize, cost_a, cost_b)


def parse(raw) -> list[Machine]:
    machines = []
    for mac_str in raw.strip().split("\n\n"):
        machine = parse_machine(mac_str)
        machines.append(machine)
    return machines


def get_solutions(mac: Machine) -> Iterator[tuple[int, int]]:
    ax, ay = mac.move_a
    bx, by = mac.move_b
    prizex, prizey = mac.prize

    for a_presses in range(101):
        for b_presses in range(101):
            x = a_presses * ax + b_presses * bx
            y = a_presses * ay + b_presses * by
            if (x, y) == mac.prize:
                yield a_presses, b_presses
            if x > prizex or y > prizey:
                break


def solve(mac: Machine) -> int:
    min_cost = None

    for a_presses, b_presses in get_solutions(mac):
        cost = a_presses * mac.cost_a + b_presses * mac.cost_b
        if min_cost is None or cost < min_cost:
            min_cost = cost

    if min_cost is None:
        raise NoSolution
    return min_cost


def main(puzzle_input):
    machines: list[Machine] = parse(puzzle_input)
    total = 0
    for m in machines:
        try:
            tokens = solve(m)
            total += tokens
        except NoSolution:
            pass
    print(total)


if __name__ == "__main__":
    # main(_input_sm)
    main(_input_lg)
