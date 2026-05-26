provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "vendor_server" {

  ami           = "ami-0c1ac8a41498c1a9c"
  instance_type = "t3.micro"
  key_name      = "vendor-key"

  security_groups = [aws_security_group.vendor_sg.name]

  tags = {
    Name = "vendor-onboarding-server"
  }
}

resource "aws_security_group" "vendor_sg" {

  name = "vendor-security-group"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
