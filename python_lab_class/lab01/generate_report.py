from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


OUTPUT = Path("文献摘要标准化清洗程序设计说明.docx")


def run(text):
    return (
        '<w:r><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" '
        'w:eastAsia="DengXian"/><w:sz w:val="21"/></w:rPr>'
        f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    )


def paragraph(text="", style=None, code=False):
    properties = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    if code:
        content = run(text)
    else:
        content = (
            '<w:r><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" '
            'w:eastAsia="DengXian"/><w:sz w:val="21"/></w:rPr>'
            f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
        )
    return f'<w:p>{properties}{content}</w:p>'


def table(rows, widths):
    columns = "".join(f'<w:gridCol w:w="{width}"/>' for width in widths)
    body = []
    for row_index, row in enumerate(rows):
        cells = []
        for index, value in enumerate(row):
            shade = '<w:shd w:fill="D9EAF7"/>' if row_index == 0 else ""
            cells.append(
                '<w:tc><w:tcPr>'
                f'<w:tcW w:w="{widths[index]}" w:type="dxa"/>{shade}'
                '</w:tcPr>'
                f'{paragraph(value)}'
                '</w:tc>'
            )
        body.append('<w:tr>' + ''.join(cells) + '</w:tr>')
    return (
        '<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>'
        '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="808080"/>'
        '<w:left w:val="single" w:sz="4" w:color="808080"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="808080"/>'
        '<w:right w:val="single" w:sz="4" w:color="808080"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="B0B0B0"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="B0B0B0"/>'
        '</w:tblBorders></w:tblPr>'
        f'<w:tblGrid>{columns}</w:tblGrid>{"".join(body)}</w:tbl>'
    )


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def document_xml():
    content = []
    content.append(paragraph("文献摘要标准化清洗程序", "Title"))
    content.append(paragraph("设计说明与标准库调研报告", "Subtitle"))
    content.append(paragraph("课程作业：Python 字符串处理"))
    content.append(paragraph("实现文件：main.py、processfun.py"))
    content.append(paragraph("文档生成日期：" + datetime.now().strftime("%Y-%m-%d")))
    content.append(page_break())

    content.append(paragraph("1. 作业理解与目标", "Heading1"))
    content.append(paragraph(
        "本作业面向从 Web of Science 等学术数据库导出的文献摘要。摘要可能包含首尾空白、重复空格、大小写混用、无关符号以及数字等内容。程序需要将文本规范化，并提供分类统计、关键词统计和最长公共前缀提取功能。"
    ))
    content.append(paragraph("本程序的输入方式包括两种：输入文本文件名读取摘要，或直接在控制台输入包含空格的摘要文本。程序将处理后的结果写入 output.txt，并在控制台显示统计信息。"))
    content.append(table([
        ["功能", "设计目标", "当前对应函数"],
        ["基础清洗", "去除首尾空白，将连续空白合并为一个空格", "basic_clean"],
        ["敏感字符过滤", "保留需要的字符，删除或替换无关特殊符号", "char_filter"],
        ["分词", "识别英文单词、数字和指定标点，为后续处理提供 token", "tokenize"],
        ["分类统计", "统计单词、数字、标点和高频二词词组", "char_classify_count、phrase_store"],
        ["大小写标准化", "句首英文单词首字母大写，其余英文单词小写", "Tokens2Sentence、case_normalization"],
        ["关键词统计", "不区分大小写统计用户指定词或短语", "specify_words"],
        ["最长公共前缀", "比较两个文献编号的公共开头", "compare"],
    ], [1700, 3400, 2000]))

    content.append(paragraph("2. 标准库调研过程", "Heading1"))
    content.append(paragraph(
        "题目要求不使用第三方库。因此，在功能设计前先将需求拆分为文本匹配、词频计数、字符类别判断、文件路径判断和控制台交互五类任务，再查阅 Python 官方标准库中对应模块及内建函数的接口说明。调研时不引入 jieba、pandas、nltk、regex 等第三方包，也不依赖外部服务。"
    ))
    content.append(paragraph("调研步骤如下："))
    content.append(paragraph("（1）针对空白合并、字符白名单过滤和英文单词识别，调研 re 模块的 re.sub、re.findall、re.fullmatch。"))
    content.append(paragraph("（2）针对高频词组计数，调研 collections.Counter 的可迭代对象计数能力。"))
    content.append(paragraph("（3）针对标点类别判断，调研 string.punctuation 常量。"))
    content.append(paragraph("（4）针对文件输入，调研 os.path.isfile、open 和 UTF-8 编码参数。"))
    content.append(paragraph("（5）针对交互和输出，调研 input、print、str.lower、str.capitalize、str.count、zip、min 等内建函数或字符串方法。"))
    content.append(table([
        ["标准库/内建能力", "调研内容", "在程序中的用途", "选择原因"],
        ["re", "正则替换、提取、完整匹配", "清洗、过滤、分词、英文词判断", "可声明字符规则，适合格式不稳定的文本"],
        ["collections.Counter", "统计可迭代对象中元素出现次数", "统计相邻二词词组出现次数", "无需手写字典累加，代码简洁"],
        ["string", "string.punctuation 的 ASCII 标点集合", "统计标点 token", "标准库提供，语义明确"],
        ["os.path", "isfile 判断路径是否为普通文件", "区分文件名输入与直接文本输入", "避免对不存在路径直接打开"],
        ["open / pathlib", "UTF-8 文本读写与路径表示", "读取摘要、输出 output.txt", "内建能力，满足本地文件处理"],
        ["str 方法", "strip、lower、count、capitalize", "标准化与关键词统计", "无需额外依赖，适合基础字符串处理作业"],
    ], [1350, 2250, 2200, 1300]))
    content.append(paragraph("本报告的 Word 文件同样未使用第三方库生成：生成脚本仅使用 Python 标准库中的 zipfile、xml.sax.saxutils、pathlib 和 datetime，按 Office Open XML 的最小文件结构打包为 .docx。"))

    content.append(paragraph("3. 功能规划与程序流程", "Heading1"))
    content.append(paragraph("总体流程：获取输入 -> 基础清洗与字符过滤 -> 分词 -> 分类统计 -> 句子切分与大小写标准化 -> 写入 output.txt -> 关键词统计 -> 最长公共前缀输出。"))
    content.append(paragraph("规划原则：同一份 token 列表供统计、句子重组和关键词查询使用，避免不同阶段对文本作不一致的处理；关键词也需要执行与正文相近的规范化，以处理 MM-LLM 这类包含连接符的术语。"))
    content.append(table([
        ["阶段", "输入", "处理", "输出"],
        ["输入", "文件名或控制台文本", "os.path.isfile 判断输入类型", "原始摘要字符串"],
        ["预处理", "原始摘要", "替换无关字符，压缩空白", "规范化文本"],
        ["分词", "规范化文本", "正则提取英文词、数字、逗号、句号", "tokens 列表"],
        ["统计", "tokens", "分类计数和二词短语 Counter", "控制台统计结果"],
        ["输出文本", "tokens", "按句切分、统一大小写、恢复标点空格", "output.txt"],
        ["查询与比较", "关键词、两个编号", "关键词计数、逐字符比较", "控制台结果"],
    ], [1100, 1800, 3000, 1200]))

    content.append(paragraph("4. 关键实现说明", "Heading1"))
    content.append(paragraph("4.1 基础清洗与过滤", "Heading2"))
    content.append(paragraph("basic_clean 使用正则表达式 \\s+ 匹配一个或多个空白字符，替换为单个空格，再调用 strip 删除首尾空白。char_filter 使用白名单规则处理无关符号，并以空格替换被移除的符号，避免 deep*learning 这类内容直接拼接为 deeplearning。"))
    content.append(paragraph("4.2 分词与统计", "Heading2"))
    content.append(paragraph("tokenize 使用 [A-Za-z]+ 识别完整英文单词，使用 \\d+ 识别连续数字，避免旧实现将 computer 拆成多个字母。phrase_store 在同一句子的相邻英文单词间组成二词词组，统一转为小写后交给 Counter 计数；出现次数不少于 3 的词组被视为高频词组。"))
    content.append(paragraph("4.3 大小写标准化与输出拼接", "Heading2"))
    content.append(paragraph("Tokens2Sentence 以句末标点切分 token 列表。case_normalization 逐个处理 token：英文单词先转小写，句首英文单词再首字母大写。_join_tokens 在逗号和句号前删除多余空格，在普通 token 之间添加一个空格，因此输出格式如：Fault diagnosis, method validation."))
    content.append(paragraph("4.4 关键词统计与 MM-LLM 处理", "Heading2"))
    content.append(paragraph("关键词统计先将正文连接为小写字符串。用户输入的关键词会被规范化：将非字母、非数字、非中文字符替换为空格，再合并空白并转小写。因此 MM-LLM、mm llm 与 Mm_Llm 均会归一为 mm llm；这使关键词形式与正文的分词结果一致，能够正确统计。随后使用 str.count 计算出现次数。"))
    content.append(paragraph("4.5 最长公共前缀", "Heading2"))
    content.append(paragraph("compare 从两个字符串的第一个字符开始逐位比较。字符相同则追加到 prefix，遇到不同字符立即结束。循环上限为两个字符串长度的较小值，时间复杂度为 O(min(m, n))，额外空间为保存结果所需空间。"))

    content.append(paragraph("5. 测试规划与结果", "Heading1"))
    content.append(paragraph("测试覆盖正常文本、空白字符、混合大小写、特殊符号、数字、高频短语、关键词变体和无公共前缀等场景。已执行 python -m py_compile main.py processfun.py，两个源文件可通过语法编译检查；同时使用 abstract.txt 进行了文件输入的端到端测试。"))
    content.append(table([
        ["测试项", "示例输入", "预期结果"],
        ["空白清洗", "  A   B  ", "得到 A B"],
        ["特殊字符", "fault@diagnosis", "特殊字符被移除且词不粘连"],
        ["大小写", "TRADITIONAL METHOD.", "Traditional method."],
        ["高频词组", "fault diagnosis 重复 3 次", "fault diagnosis 被识别为高频词组"],
        ["关键词变体", "MM-LLM / mm llm / Mm_Llm", "均按 mm llm 统计"],
        ["最长公共前缀", "0x01010007121 与 0x01010007210", "0x01010007"],
    ], [1300, 3000, 2800]))

    content.append(paragraph("6. 约束符合性与后续完善", "Heading1"))
    content.append(paragraph("本程序的业务实现仅依赖 Python 标准库，没有安装或导入第三方库，满足题目限制。核心文本处理依靠 re，计数依靠 collections.Counter，文件及控制台交互使用内建能力和 os.path。"))
    content.append(paragraph("需要注意的当前实现限制："))
    content.append(paragraph("（1）作业要求保留中文，而当前 processfun.py 中 char_filter 的白名单为 [^A-Za-z0-9,-.\\s]，尚未把中文范围加入规则；如果要完整满足该条，应在过滤和分词规则中加入 \\u4e00-\\u9fff。"))
    content.append(paragraph("（2）当前高频词组定义为相邻英文二词短语，不能自动发现三词及以上固定搭配；如题目要求更广泛的 n-gram 统计，可增加词组长度参数。"))
    content.append(paragraph("（3）关键词使用 str.count，可能匹配到更长单词内部的相同字符。例如搜索 art 也会匹配 article。若需要严格的词边界匹配，可继续使用 re 构造边界规则。"))
    content.append(paragraph("（4）当前分词与输出主要面向英文摘要；如需自然地处理中文句子，还可增加中文句末符号和中文标点规则。"))

    content.append(paragraph("7. 总结", "Heading1"))
    content.append(paragraph("本作业围绕字符串处理完成了文献摘要标准化、分类统计、关键词查询和最长公共前缀提取。设计中先依据功能调研 Python 标准库，再将每项需求映射为独立函数，最终形成从输入、清洗、分词到输出和查询的完整流程。该方案结构清晰、依赖少，适合作为基础 Python 字符串处理课程作业的实现。"))

    section = (
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="708" w:footer="708" w:gutter="0"/>'
        '</w:sectPr>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f'<w:body>{"".join(content)}{section}</w:body></w:document>'
    )


STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="DengXian"/><w:sz w:val="21"/></w:rPr></w:rPrDefault></w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:pPr><w:jc w:val="center"/><w:spacing w:after="240"/></w:pPr><w:rPr><w:b/><w:rFonts w:eastAsia="DengXian"/><w:sz w:val="36"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:pPr><w:jc w:val="center"/><w:spacing w:after="360"/></w:pPr><w:rPr><w:rFonts w:eastAsia="DengXian"/><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="260" w:after="120"/></w:pPr><w:rPr><w:b/><w:rFonts w:eastAsia="DengXian"/><w:sz w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="180" w:after="80"/></w:pPr><w:rPr><w:b/><w:rFonts w:eastAsia="DengXian"/><w:sz w:val="24"/></w:rPr></w:style>
</w:styles>'''


def write_docx():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = {
        "[Content_Types].xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>''',
        "_rels/.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''',
        "word/_rels/document.xml.rels": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>''',
        "word/document.xml": document_xml(),
        "word/styles.xml": STYLES,
        "docProps/core.xml": f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>文献摘要标准化清洗程序设计说明</dc:title><dc:creator>学生</dc:creator><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>''',
        "docProps/app.xml": '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Python standard library</Application></Properties>''',
    }
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
        for path, content in files.items():
            archive.writestr(path, content.encode("utf-8"))


if __name__ == "__main__":
    write_docx()
    print(OUTPUT.resolve())
