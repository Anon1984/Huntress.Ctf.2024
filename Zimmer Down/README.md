
# Zimmer Down CTF Write-Up

### Challenge Description

A user interacted with a suspicious file on one of our hosts. The only thing I managed to grab was the user's registry hive. Are they hiding any secrets?

### Provided File

- **`NTUSER.DAT`** - the registry hive of the user.

---

### Solution

#### Step 1: Analyzing the Registry Hive

I began by examining the `NTUSER.DAT` file to search for suspicious activities or hidden secrets. Using **Regripper** (version 4.0), I parsed the registry file and generated a report with various key entries.

#### Step 2: Inspecting the Regripper Report

Upon reviewing the Regripper report, I identified some key findings:

- **Recently Accessed Files**:
  - In the registry path `Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`, I found an entry for a `.b62` file:
    ```
    VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF.b62
    ```
  - This file had an unusual name and a `.b62` extension, suggesting Base62 encoding.

- **Suspicion of Encoding**:
  - Given the `.b62` extension, I suspected that the filename might be Base62 encoded, commonly used to obfuscate data in CTFs.

#### Step 3: Decoding the `.b62` Filename

To decode the filename, I used **CyberChef** to convert the Base62-encoded string:
   ```
   Input: VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF
   Output: flag{4b676ccc1070be66b1a15dB601c8d500}
   ```

This revealed the flag `flag{4b676ccc1070be66b1a15dB601c8d500}`, which appeared to be the hidden secret.

---

### Conclusion

By analyzing the `NTUSER.DAT` registry hive, I located a Base62-encoded filename that, when decoded, revealed the flag. The steps I took included:

1. Extracting recent file entries from the registry.
2. Identifying the `.b62` extension and decoding it as Base62.
3. Using CyberChef to decode the filename and retrieve the flag.

### Final Flag

```
flag{4b676ccc1070be66b1a15dB601c8d500}
```

This solution demonstrates how I used registry analysis and encoding/decoding techniques to uncover hidden information in forensic challenges.

---

### Files

- `NTUSER.DAT` – Provided by the challenge
- `report.txt` – Regripper output file (not included in this repo)

### Tools Used

- [Regripper](https://github.com/keydet89/RegRipper2.8)
- [CyberChef](https://gchq.github.io/CyberChef/)

---

### Author

Written by [Your GitHub Username]
