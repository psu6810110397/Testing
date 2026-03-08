import unittest
from unittest.mock import patch

# ดึงฟังก์ชันมาจากไฟล์ production/cipherstub.py [cite: 51]
from production.cipherstub import caesarCipher, interactive_cipher


class TestCipherStub(unittest.TestCase):
    """คลาสสำหรับทดสอบที่ใช้โครงสร้าง Arrange-Act-Assert (AAA) [cite: 87]"""

    def test_caesar_cipher_normal(self):
        # Arrange: เตรียมข้อมูลนำเข้าและผลลัพธ์ที่คาดหวัง [cite: 88]
        s = "middle-Outz"
        k = 2
        expected = "okffng-Qwvb"

        # Act: เรียกใช้งานฟังก์ชัน [cite: 91]
        result = caesarCipher(s, k)

        # Assert: ตรวจสอบความถูกต้อง [cite: 94]
        self.assertEqual(result, expected)

    def test_caesar_cipher_wrap_around(self):
        # Arrange: กรณีเลื่อนแล้ววนจาก z กลับไป a [cite: 1]
        s = "abcZ"
        k = 1
        expected = "bcdA"

        # Act
        result = caesarCipher(s, k)

        # Assert
        self.assertEqual(result, expected)

    # ---------------------------------------------------------
    # ส่วนการทำ Stub (Indirect Input) เพื่อคะแนนพิเศษ [cite: 213]
    # ---------------------------------------------------------
    @patch("builtins.input")  # ใช้ patch เพื่อสร้าง Stub แทนการรับค่าจริงจากคีย์บอร์ด [cite: 226]
    def test_interactive_cipher_with_stub(self, mock_input):
        # Arrange: กำหนดค่าที่ต้องการให้ input() คืนค่าออกมาตามลำดับ [cite: 213]
        # ครั้งแรกคืนค่า 'Hello', ครั้งที่สองคืนค่า '2'
        mock_input.side_effect = ["Hello", "2"]
        expected_output = "Jgnnq"

        # Act: รันฟังก์ชันที่มีการใช้ input()
        result = interactive_cipher()

        # Assert: ตรวจสอบสถานะ (State Verification) [cite: 214]
        self.assertEqual(result, expected_output)
        # ตรวจสอบว่ามีการเรียกใช้ input() ครบตามจำนวนที่คาดไว้หรือไม่
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
