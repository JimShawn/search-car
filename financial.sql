create table user{

	}


create table dept{
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	'dept_code' varchar(8) not null COMMENT '部门编码',
	'parent_dept_id' int(10) not null COMMENT '上级部门id',
	'status' tinyint(2) null COMMENT '1，有效，0无效',
	`created_time` int(10) NOT NULL COMMENT '创建时间',
	PRIMARY KEY (`id`)
	}ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;




create table `product`(
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `product_template_id` int(10) not null COMMENT '产品模板id，关联自身，当自身为产品模板时，为0',
  `name` varchar(50) NOT NULL,
  `product_type` int(2) NOT NULL COMMENT '产品类型，1标识二手车贷款，其他的之后添加',
  `payback_type` int(2) NOT NULL COMMENT '还款方式，1为等额本息，其他的之后补充',
  `min_available_rate` tinyint(2) NOT NULL COMMENT '最小可用贷款成数，',
  `max_available_rate` tinyint(2) NOT NULL COMMENT '最大可用贷款成数',
  `available_terms` varchar(50) NOT NULL COMMENT '可贷期数，具体数字加逗号分隔',
  `loan_policy` int(2) NOT NULL COMMENT '贷款政策，1，抵押放款，2过户放款',
  `loan_benift_per_month` varchar(50) NOT NULL COMMENT '贷款月利率，float数字加逗号区分',
  `modified_time` int(10) NOT NULL  COMMENT '修改时间',
  `created_time` int(10) NOT NULL  COMMENT '创建时间',
  `creator_uid` int(10) NOT NULL COMMENT '创建人id',
  `status` int(2) NOT NULL COMMENT '产品状态，1，创建，2，审批通过，3，审批拒绝，4，废弃',
  `city_id` int(10) not null COMMENT '适用城市id,0表示当前是模板，其他时候表示具体城市id',
  PRIMARY KEY (`id`)

)ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

create table `product_log`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`product_id` int(10) NOT null COMMENT '产品id', 
	`operator_uid` int(10) not null COMMENT '操作人id',
	`operate_type` tinyint(3) NOT null COMMENT '操作类型，1创建，2，审批通过，3，审批拒绝，4，废弃',
	`created_time` int(10) NOT NULL  COMMENT '创建时间',
	`remark` varchar(200) COMMENT '操作备注'
	PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- 产品审批职责表

create table `loan`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`product_id` COMMENT '产品id',
	`product_name` COMMENT '产品名称',
	`product_type` COMMENT '产品类型',
	`loan_rate` int(2) COMMENT '成数',
	`loan_terms` int(2) COMMENT '期数',
	`loan_benift_per_month` float(6,2) COMMENT '月利率',
	`car_price` float(10,2) COMMENT '成交价',
	`downpayment` float(10,2) COMMENT '首付',
	`loan_amount` float(10,2) COMMENT '贷款金额',
	`payment_per_month` float(10,2) COMMENT '月还款金额',
	`apply_pic_url` varchar(1000) COMMENT '多张图片链接通过|||分隔',
	`remark` varchar(200) COMMENT '申请备注',
	`ext_source_id` int(10) COMMENT '来源id',
	`ext_applicant_id` int(10) COMMENT '来源id',
	`ext_co_applicant_id` int(10) COMMENT '来源id',
	`ext_guarantor_id` int(10) COMMENT '来源id',
	`ext_car_id` int(10) COMMENT '来源id',
	`created_time` int(10) NOT NULL  COMMENT '创建时间',
	`status` tinyint(2) COMMENT '状态,0草稿，1待审核,2退回待修改，3,初审拒绝，4,初审通过/复审待定价，5复审已定价，6复审拒绝,7复审通过/待签约，8已签约，9放弃签约，10确认放弃',
	PRIMARY KEY (`id`)
)

create table `loan_source`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`city_id` int(10) NOT null COMMENT '来源省市',
	`apply_source` int(2) NOT null COMMENT '来源渠道',
	`source_person_name` varchar(10) COMMENT '来源人姓名',
	`source_person_tel` varchar(15) COMMENT '来源人电话',
	PRIMARY KEY (`id`)
)


create table loan_applicant(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`applicant_name` varchar(10) COMMENT '申请人姓名',
	`applicant_tel`
	`certificate_type` int(2)
	`certificate_num`
	`marrige` tinyint(2)
	`income_per_month`
	`certificate_file_ids` varchar(100) COMMENT '证件图片id列表',
	`qualification_file_ids` varchar(200) COMMENT '学历',
	`income_file_ids` varchar(500) COMMENT '收入及财力',
	`house_file_ids` varchar(200) COMMENT '房产',
	`car_file_ids` varchar(200) COMMENT '车辆',
	`other_file_ids` varchar(200) COMMENT '其他'
)

create table `loan_co_applicant`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`certificate_file_ids` varchar(100) COMMENT '证件图片id列表',
	`income_file_ids` varchar(500) COMMENT '收入及财力',
	`house_file_ids` varchar(200) COMMENT '房产',
	`other_file_ids` varchar(200) COMMENT '其他'
)

create table `loan_guarantor`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`certificate_file_ids` varchar(100) COMMENT '证件图片id列表',
	`income_file_ids` varchar(500) COMMENT '收入及财力',
	`house_file_ids` varchar(200) COMMENT '房产',
	`other_file_ids` varchar(200) COMMENT '其他'
)

create table `loan_car`(
	`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
	`vin` char(20) COMMENT '车架号'
	`manufacturers` varchar(10) COMMENT '厂家'
	`brand` varchar(10) COMMENT '品牌',
	`series` varchar(50) COMMENT ''
	`miles` float(6,2) COMMENT '',
	`registration_certificate_file_ids` varchar(100),
	`license_file_ids` varchar(100),
	`car_file_ids` varchar(2000)
)





