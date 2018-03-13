
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'RSHIFT LPAREN STAR_ASSIGN MINUS_ASSIGN LSHIFT_ASSIGN LOGICAL_AND LSHIFT AND_XOR_ASSIGN MINUS DOT LCURL RSQUARE INCR RPAREN MORE_EQUALS RCURL LESS_EQUALS QUICK_ASSIGN AND_ASSIGN COMMA DECR COLON NOT_ASSIGN ASSIGN PLUS XOR DIVIDE EQUALS STAR DIVIDE_ASSIGN LSQUARE GREATER AND MOD_ASSIGN SEMICOLON XOR_ASSIGN RSHIFT_ASSIGN OR_ASSIGN LESSER LOGICAL_OR AND_XOR PLUS_ASSIGN NOT OR MOD STRING FLOAT HEX RUNE OCTAL INTEGER IMAGINARY IDENTIFIER CASE RETURN GOTO FOR PACKAGE DEFAULT RANGE ELSE BREAK SWITCH CONTINUE FUNC IMPORT VAR CONST IF TYPE STRUCTstart : PackageClause SEMICOLON ImportDeclRep TopLevelDeclRepPackageClause : PACKAGE PackageNamePackageName : IDENTIFIER PackageNameDotOpt : DOT\n                        | PackageName\n                        | epsilonImportDeclRep : epsilon\n           | ImportDeclRep ImportDecl SEMICOLONImportDecl : IMPORT ImportSpec\n          | IMPORT LPAREN ImportSpecRep RPAREN  ImportSpecRep : ImportSpecRep ImportSpec SEMICOLON\n            | epsilon  ImportSpec : PackageNameDotOpt ImportPath  ImportPath : STRING TopLevelDeclRep : TopLevelDeclRep TopLevelDecl SEMICOLON\n                     | epsilonTopLevelDecl : Declaration\n                  | FunctionDeclDeclaration : ConstDecl\n                 | TypeDecl\n                 | VarDeclConstDecl : CONST ConstSpec\n                 | CONST LPAREN ConstSpecRep RPARENConstSpecRep : ConstSpecRep ConstSpec SEMICOLON\n                    | epsilonConstSpec : IdentifierList TypeExprListOptTypeExprListOpt : TypeOpt ASSIGN ExpressionList\n                       | epsilonIdentifierList : IDENTIFIER IdentifierRepIdentifierRep : IdentifierRep COMMA IDENTIFIER\n                     | epsilonExpressionList : Expression ExpressionRepExpressionRep : ExpressionRep COMMA Expression\n                     | epsilonFunctionDecl : FUNC FunctionName Function\n                    | FUNC FunctionName SignatureFunctionName : IDENTIFIERFunction : Signature FunctionBodyFunctionBody : BlockTypeDecl : TYPE TypeSpec\n                | TYPE LPAREN TypeSpecRep RPARENTypeSpecRep : TypeSpecRep TypeSpec SEMICOLON\n                   | epsilonTypeSpec : AliasDecl\n                | TypeDefAliasDecl : IDENTIFIER ASSIGN TypeTypeDef : IDENTIFIER TypeVarDecl : epsilonExpression : epsilonTypeOpt : Type\n               | epsilonType : epsilonSignature : epsilonBlock : epsilonepsilon : '
    
_lr_action_items = {'CONST':([4,7,8,9,10,23,34,],[-55,-7,-55,13,-16,-8,-15,]),'STRING':([6,12,24,26,27,28,29,42,43,74,],[-3,-55,-55,-6,-5,45,-4,-12,-55,-11,]),'SEMICOLON':([1,4,5,6,7,8,9,10,11,14,15,16,17,18,19,21,23,25,30,32,33,34,35,36,37,38,40,41,44,45,49,50,52,53,54,55,56,59,60,61,62,63,64,65,66,68,69,70,71,72,73,76,77,78,79,81,82,83,84,],[4,-55,-2,-3,-7,-55,-55,-16,23,-18,34,-17,-19,-20,-48,-21,-8,-9,-22,-55,-55,-15,-37,-55,-45,-44,-40,-55,-13,-14,-28,-26,-31,-29,-35,-53,-36,-52,-47,-55,-10,74,75,-23,-55,-38,-54,-39,-41,80,-46,-27,-49,-55,-30,-32,-34,-55,-33,]),'PACKAGE':([0,],[2,]),'RPAREN':([24,31,39,42,43,46,47,57,58,74,75,80,],[-55,-55,-55,-12,62,65,-25,71,-43,-11,-24,-42,]),'COMMA':([33,52,53,66,77,78,79,81,82,83,84,],[-55,-31,67,-55,-49,-55,-30,83,-34,-55,-33,]),'FUNC':([4,7,8,9,10,23,34,],[-55,-7,-55,20,-16,-8,-15,]),'LPAREN':([12,13,22,],[24,31,39,]),'IMPORT':([4,7,8,23,],[-55,-7,12,-8,]),'IDENTIFIER':([2,12,13,20,22,24,31,39,42,43,46,47,57,58,67,74,75,80,],[6,6,33,35,41,-55,-55,-55,-12,6,33,-25,41,-43,79,-11,-24,-42,]),'TYPE':([4,7,8,9,10,23,34,],[-55,-7,-55,22,-16,-8,-15,]),'ASSIGN':([32,33,41,48,49,51,52,53,79,],[-55,-55,61,-50,-51,66,-31,-29,-30,]),'DOT':([12,24,42,43,74,],[29,-55,-12,29,-11,]),'$end':([3,4,7,8,9,10,23,34,],[0,-55,-7,-55,-1,-16,-8,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'FunctionBody':([56,],[68,]),'ExpressionRep':([78,],[81,]),'PackageName':([2,12,43,],[5,27,27,]),'FunctionDecl':([9,],[14,]),'TopLevelDecl':([9,],[15,]),'IdentifierList':([13,46,],[32,32,]),'Expression':([66,83,],[78,84,]),'Type':([32,41,61,],[48,60,73,]),'ImportDecl':([8,],[11,]),'FunctionName':([20,],[36,]),'Function':([36,],[54,]),'PackageClause':([0,],[1,]),'ImportSpec':([12,43,],[25,63,]),'AliasDecl':([22,57,],[38,38,]),'ImportDeclRep':([4,],[8,]),'start':([0,],[3,]),'Declaration':([9,],[16,]),'TopLevelDeclRep':([8,],[9,]),'TypeDecl':([9,],[18,]),'ConstSpec':([13,46,],[30,64,]),'epsilon':([4,8,9,12,24,31,32,33,36,39,41,43,56,61,66,78,83,],[7,10,19,26,42,47,49,52,55,58,59,26,69,59,77,82,77,]),'ExpressionList':([66,],[76,]),'ImportSpecRep':([24,],[43,]),'Signature':([36,],[56,]),'TypeOpt':([32,],[51,]),'Block':([56,],[70,]),'ImportPath':([28,],[44,]),'TypeDef':([22,57,],[37,37,]),'ConstDecl':([9,],[17,]),'VarDecl':([9,],[21,]),'TypeSpecRep':([39,],[57,]),'IdentifierRep':([33,],[53,]),'TypeExprListOpt':([32,],[50,]),'ConstSpecRep':([31,],[46,]),'TypeSpec':([22,57,],[40,72,]),'PackageNameDotOpt':([12,43,],[28,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> PackageClause SEMICOLON ImportDeclRep TopLevelDeclRep','start',4,'p_start','parser.py',10),
  ('PackageClause -> PACKAGE PackageName','PackageClause',2,'p_package_clause','parser.py',17),
  ('PackageName -> IDENTIFIER','PackageName',1,'p_package_name','parser.py',22),
  ('PackageNameDotOpt -> DOT','PackageNameDotOpt',1,'p_package_name_dot_opt','parser.py',26),
  ('PackageNameDotOpt -> PackageName','PackageNameDotOpt',1,'p_package_name_dot_opt','parser.py',27),
  ('PackageNameDotOpt -> epsilon','PackageNameDotOpt',1,'p_package_name_dot_opt','parser.py',28),
  ('ImportDeclRep -> epsilon','ImportDeclRep',1,'p_import_decl_rep','parser.py',38),
  ('ImportDeclRep -> ImportDeclRep ImportDecl SEMICOLON','ImportDeclRep',3,'p_import_decl_rep','parser.py',39),
  ('ImportDecl -> IMPORT ImportSpec','ImportDecl',2,'p_import_decl','parser.py',46),
  ('ImportDecl -> IMPORT LPAREN ImportSpecRep RPAREN','ImportDecl',4,'p_import_decl','parser.py',47),
  ('ImportSpecRep -> ImportSpecRep ImportSpec SEMICOLON','ImportSpecRep',3,'p_import_spec_rep','parser.py',54),
  ('ImportSpecRep -> epsilon','ImportSpecRep',1,'p_import_spec_rep','parser.py',55),
  ('ImportSpec -> PackageNameDotOpt ImportPath','ImportSpec',2,'p_import_spec','parser.py',62),
  ('ImportPath -> STRING','ImportPath',1,'p_import_path','parser.py',66),
  ('TopLevelDeclRep -> TopLevelDeclRep TopLevelDecl SEMICOLON','TopLevelDeclRep',3,'p_toplevel_decl_rep','parser.py',73),
  ('TopLevelDeclRep -> epsilon','TopLevelDeclRep',1,'p_toplevel_decl_rep','parser.py',74),
  ('TopLevelDecl -> Declaration','TopLevelDecl',1,'p_toplevel_decl','parser.py',81),
  ('TopLevelDecl -> FunctionDecl','TopLevelDecl',1,'p_toplevel_decl','parser.py',82),
  ('Declaration -> ConstDecl','Declaration',1,'p_decl','parser.py',86),
  ('Declaration -> TypeDecl','Declaration',1,'p_decl','parser.py',87),
  ('Declaration -> VarDecl','Declaration',1,'p_decl','parser.py',88),
  ('ConstDecl -> CONST ConstSpec','ConstDecl',2,'p_const_decl','parser.py',95),
  ('ConstDecl -> CONST LPAREN ConstSpecRep RPAREN','ConstDecl',4,'p_const_decl','parser.py',96),
  ('ConstSpecRep -> ConstSpecRep ConstSpec SEMICOLON','ConstSpecRep',3,'p_const_spec_rep','parser.py',103),
  ('ConstSpecRep -> epsilon','ConstSpecRep',1,'p_const_spec_rep','parser.py',104),
  ('ConstSpec -> IdentifierList TypeExprListOpt','ConstSpec',2,'p_const_spec','parser.py',111),
  ('TypeExprListOpt -> TypeOpt ASSIGN ExpressionList','TypeExprListOpt',3,'p_type_expr_list','parser.py',115),
  ('TypeExprListOpt -> epsilon','TypeExprListOpt',1,'p_type_expr_list','parser.py',116),
  ('IdentifierList -> IDENTIFIER IdentifierRep','IdentifierList',2,'p_identifier_list','parser.py',123),
  ('IdentifierRep -> IdentifierRep COMMA IDENTIFIER','IdentifierRep',3,'p_identifier_rep','parser.py',127),
  ('IdentifierRep -> epsilon','IdentifierRep',1,'p_identifier_rep','parser.py',128),
  ('ExpressionList -> Expression ExpressionRep','ExpressionList',2,'p_expr_list','parser.py',135),
  ('ExpressionRep -> ExpressionRep COMMA Expression','ExpressionRep',3,'p_expr_rep','parser.py',139),
  ('ExpressionRep -> epsilon','ExpressionRep',1,'p_expr_rep','parser.py',140),
  ('FunctionDecl -> FUNC FunctionName Function','FunctionDecl',3,'p_func_decl','parser.py',150),
  ('FunctionDecl -> FUNC FunctionName Signature','FunctionDecl',3,'p_func_decl','parser.py',151),
  ('FunctionName -> IDENTIFIER','FunctionName',1,'p_func_name','parser.py',155),
  ('Function -> Signature FunctionBody','Function',2,'p_func','parser.py',159),
  ('FunctionBody -> Block','FunctionBody',1,'p_func_body','parser.py',163),
  ('TypeDecl -> TYPE TypeSpec','TypeDecl',2,'p_type_decl','parser.py',170),
  ('TypeDecl -> TYPE LPAREN TypeSpecRep RPAREN','TypeDecl',4,'p_type_decl','parser.py',171),
  ('TypeSpecRep -> TypeSpecRep TypeSpec SEMICOLON','TypeSpecRep',3,'p_type_spec_rep','parser.py',178),
  ('TypeSpecRep -> epsilon','TypeSpecRep',1,'p_type_spec_rep','parser.py',179),
  ('TypeSpec -> AliasDecl','TypeSpec',1,'p_type_spec','parser.py',186),
  ('TypeSpec -> TypeDef','TypeSpec',1,'p_type_spec','parser.py',187),
  ('AliasDecl -> IDENTIFIER ASSIGN Type','AliasDecl',3,'p_alias_decl','parser.py',191),
  ('TypeDef -> IDENTIFIER Type','TypeDef',2,'p_type_def','parser.py',198),
  ('VarDecl -> epsilon','VarDecl',1,'p_var_decl','parser.py',204),
  ('Expression -> epsilon','Expression',1,'p_expr','parser.py',209),
  ('TypeOpt -> Type','TypeOpt',1,'p_type_opt','parser.py',213),
  ('TypeOpt -> epsilon','TypeOpt',1,'p_type_opt','parser.py',214),
  ('Type -> epsilon','Type',1,'p_type','parser.py',219),
  ('Signature -> epsilon','Signature',1,'p_sign','parser.py',225),
  ('Block -> epsilon','Block',1,'p_block','parser.py',230),
  ('epsilon -> <empty>','epsilon',0,'p_empty','parser.py',235),
]
