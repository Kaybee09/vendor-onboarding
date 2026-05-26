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
