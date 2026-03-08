def caesarCipher(s, k):
    """ฟังก์ชันหลักสำหรับเข้ารหัส Caesar Cipher [cite: 199]"""
    result = []
    # ใช้ Modulo 26 เพื่อรองรับกรณี k มีค่ามากกว่าจำนวนตัวอักษรภาษาอังกฤษ [cite: 1]
    k = k % 26

    for char in s:
        # ตรวจสอบว่าเป็นตัวอักษรภาษาอังกฤษหรือไม่ [cite: 31]
        if char.isalpha():
            # กำหนดฐาน ASCII: A=65, a=97 [cite: 1]
            base = ord("A") if char.isupper() else ord("a")
            # คำนวณตำแหน่งใหม่และวนกลับมาที่ต้นแถวด้วย % 26 [cite: 1]
            shifted_char = chr((ord(char) - base + k) % 26 + base)
            result.append(shifted_char)
        else:
            # กรณีเป็นอักขระพิเศษหรือตัวเลข ให้คงไว้เช่นเดิม [cite: 1]
            result.append(char)

    return "".join(result)


def interactive_cipher():
    """ฟังก์ชันสำหรับรับค่าจาก Keyboard เพื่อใช้ทดสอบการทำ Stub (Indirect Input) [cite: 213]"""
    text = input("Enter text: ")
    step_str = input("Enter step: ")
    step = int(step_str)
    return caesarCipher(text, step)
