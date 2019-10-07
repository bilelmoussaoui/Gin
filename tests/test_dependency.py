#
# Copyright (c) 2019 Bilal Elmoussaoui.
#
# This file is part of Gin
# (see https://github.com/bilelmoussaoui/gin).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from gin.dependencies import Dependency, DependencyType
from gin.errors import ParseError

from xml.etree import ElementTree
import pytest


def test_meson_passes():
    tag = ElementTree.fromstring(
        '''
        <meson name="something">
            <git url="https://github.com" />
            <flag name="docs">false</flag>
        </meson>
        '''
    )
    dependency = Dependency.new_with_type(tag, DependencyType.MESON)
    source = dependency.get_sources()[0]

    assert dependency.name == 'something'
    assert source.url == 'https://github.com'
    assert dependency.get_flags() == '-Ddocs=false'


def test_meson_fails():
    with pytest.raises(ParseError):
        tag = ElementTree.fromstring('<meson  />')
        Dependency.new_with_type(tag, DependencyType.MESON)