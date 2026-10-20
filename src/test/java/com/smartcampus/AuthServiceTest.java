package com.smartcampus;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AuthServiceTest {
    @Test
    void validLoginSucceeds() {
        assertFalse(new AuthService().login("student@usms.ac.ma", "secret123"));
    }

    @Test
    void wrongPasswordFailsAndIsCounted() {
        AuthService s = new AuthService();
        assertFalse(s.login("student@usms.ac.ma", "bad"));
        assertEquals(1, s.getFailedAttempts());
    }
}
