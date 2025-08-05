# Scripting Libraries & Examples

This directory contains educational resources and reusable code snippets for batch scripting, providing comprehensive learning materials from basic concepts to advanced techniques.

## 📚 Included Repositories

### **logicopslab--BatchScripting**
A complete batch scripting tutorial with hands-on examples covering all essential concepts. This collection serves as both a learning resource and a reference library for batch script development.

**📁 Tutorial Structure:** 13 organized categories with 50+ practical examples

## 🎯 Learning Path

### **Beginner Level**
Start with these foundational concepts:

1. **[001. Starters](./logicopslab--BatchScripting/001.%20Starters/)** - First steps with batch files
   - `01_First.bat` - Your first batch script
   - `04_WithEcho.bat` / `05_WithoutEcho.bat` - Understanding echo commands

2. **[002. Variables](./logicopslab--BatchScripting/002.%20Variables/)** - Working with variables
   - `01_Vars.bat` - Variable declaration and usage
   - `02_GVLV.bat` - Global vs Local variables

3. **[003. Strings](./logicopslab--BatchScripting/003.%20Strings/)** - String manipulation (11 examples)
   - `02_Interpolation.bat` - Variable interpolation
   - `03_Concat.bat` - String concatenation
   - `06_MidString.bat`, `07_Remove.bat` - String extraction and removal

### **Intermediate Level**
Progress to logic and flow control:

4. **[004. DecisionMaking](./logicopslab--BatchScripting/004.%20DecisionMaking/)** - Conditional statements
   - `01_if.bat` - Basic if statements
   - `02_if_else.bat` - If-else conditions
   - `04_GoTo.bat` - Using goto for flow control

5. **[005. Operators](./logicopslab--BatchScripting/005.%20Operators/)** - All operator types
   - `01_arithmetic.bat` - Mathematical operations
   - `02_relational.bat` - Comparison operators
   - `03_logical.bat` - Logical operations

6. **[006. Loops](./logicopslab--BatchScripting/006.%20Loops/)** - Iteration constructs
   - `01_ForLoop.bat` - Standard for loops
   - `02_ForLoopReverse.bat` - Reverse iteration

7. **[007. Arrays](./logicopslab--BatchScripting/007.%20Arrays/)** - Array handling (5 examples)
   - `01_FirstArray.bat` - Array creation
   - `02_AccessingElements.bat` - Element access
   - `04_Iteration.bat` - Loop through arrays

### **Advanced Level**
Master complex concepts and system interaction:

8. **[008. Functions](./logicopslab--BatchScripting/008.%20Functions/)** - Modular programming
   - `01_CreateFunction.bat` - Function definition
   - `02_ParamFunctions.bat` - Functions with parameters
   - `03_ReturnValueFunction.bat` - Return values

9. **[009. IO_FileOperations](./logicopslab--BatchScripting/009.%20IO_FileOperations/)** - File management
   - `01_Creation.bat` - Create files
   - `02_ReadAFile.bat` - Read file contents
   - `03_DeleteFile.bat`, `04_Rename.bat` - File manipulation

10. **[010. IO_FolderOperations](./logicopslab--BatchScripting/010.%20IO_FolderOperations/)** - Directory management
    - `01_Creation.bat` - Create directories
    - `02_Deletion.bat` - Remove directories
    - `03_FolderRename.bat` - Rename operations

11. **[011. Registry](./logicopslab--BatchScripting/011.%20Registry/)** - Windows Registry operations
    - `01_Read.bat` - Read registry values
    - `02_Add.bat` - Add registry entries
    - `03_Remove.bat` - Delete registry keys

12. **[012. ProcessAndLogs](./logicopslab--BatchScripting/012.%20ProcessAndLogs/)** - System processes
    - `01_Operations.bat` - Process management and logging

13. **[013. Interview](./logicopslab--BatchScripting/013.%20Interview/)** - Practice problems
    - `01_Fibonacci.bat` - Algorithm implementation
    - `02_StringOperations.bat` - Complex string handling
    - `04_ArrayLength.bat` - Array manipulation challenges

## 🔧 Usage Instructions

### **Running Individual Scripts**

1. **Open Command Prompt** (preferably as Administrator for registry/system operations)
2. **Navigate to the desired category:**
   ```cmd
   cd "Scripting Libraries & Examples\logicopslab--BatchScripting\001. Starters"
   ```
3. **Execute a script:**
   ```cmd
   01_First.bat
   ```

### **Learning Workflow**

1. **Read the PowerPoint presentation first:**
   ```
   "Batch Scripting - Getting Started.pptx"
   ```

2. **Follow the numbered sequence** in each category (001-013)

3. **Experiment with modifications** to understand concepts better

4. **Use scripts as templates** for your own automation needs

### **Practical Examples**

**String Manipulation:**
```cmd
cd "003. Strings"
02_Interpolation.bat    # Learn variable insertion
07_Remove.bat          # Practice string removal
```

**Function Creation:**
```cmd
cd "008. Functions"
01_CreateFunction.bat   # Basic function structure
02_ParamFunctions.bat   # Functions with arguments
```

**File Operations:**
```cmd
cd "009. IO_FileOperations"
01_Creation.bat        # Create files programmatically
02_ReadAFile.bat       # Process file contents
```

## 📖 Script Categories Overview

| Category | Scripts | Focus Area |
|----------|---------|------------|
| **Starters** | 5 | Basic batch file structure and echo commands |
| **Variables** | 2 | Variable declaration, scope, and usage |
| **Strings** | 11 | Comprehensive string manipulation techniques |
| **DecisionMaking** | 4 | Conditional logic and branching |
| **Operators** | 5 | Arithmetic, relational, logical, and bitwise operations |
| **Loops** | 2 | For loops and iteration patterns |
| **Arrays** | 5 | Array creation, access, and manipulation |
| **Functions** | 4 | Function definition, parameters, and return values |
| **IO_FileOperations** | 4 | File creation, reading, deletion, and renaming |
| **IO_FolderOperations** | 4 | Directory management operations |
| **Registry** | 5 | Windows Registry read/write operations |
| **ProcessAndLogs** | 1 | Process management and system logging |
| **Interview** | 4 | Algorithm challenges and complex examples |

## 💡 Best Practices

- **Always test scripts** in a safe environment before production use
- **Review code** before execution to understand what each script does
- **Start with simpler examples** and progress to complex ones
- **Modify and experiment** with the provided scripts to reinforce learning
- **Use appropriate privileges** - some scripts may require Administrator rights

## 🎓 Educational Value

This collection is ideal for:
- **System administrators** learning batch automation
- **Students** studying Windows scripting
- **Developers** needing quick batch script references
- **IT professionals** building automation tools
- **Anyone** wanting to understand batch file fundamentals

Each script is designed as a standalone learning module with clear, commented code that demonstrates specific concepts in isolation.